from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required
import random

apple = Blueprint("apple", __name__)

mysql = None

@apple.route('/create_project')
@login_required
def create_project():
    session.pop('project_users', None)
    session.pop('project', None)
    return render_template('/project/createproject.html')

# 新しいプロジェクトを作成する
@apple.route('/create_project1')
@login_required
def create_project1():
    return render_template('/project/createproject1.html', user_id=session['user_id'])

@apple.route('/action/create_project1', methods=['POST'])
@login_required
def action_create_project1():
    userId = str(session.get("user_id"))
    uName = str(session.get("user_name"))
    conn = mysql.get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # プロジェクト情報を取得
        projectTitle = request.form.get('projectTitle')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        # collaborator = request.form.get('collaborator')
        urlInput = request.form.get('urlInput')
        sharedFolderInput = request.form.get('sharedFolderInput')
        sprint = request.form.get('sprint')

        # プロジェクト情報を保存
        cur.execute("INSERT INTO project(name, owner, start_date, finish_date, github, googleDrive, sprint) VALUES (%s, %s, %s, %s, %s, %s, %s)", (projectTitle, uName, startDate, endDate, urlInput, sharedFolderInput, sprint))
        conn.commit()

        # 直前のINSERT操作で生成されたIDを取得
        projectNumber = cur.lastrowid
        
        cur.execute("INSERT INTO project_users(projectName, userId, projectNumber) VALUES (%s, %s, %s)", (projectTitle, userId, projectNumber))
        conn.commit()

    cur.close()
    conn.close()
    
    session['project_users'] = uName
    session["project"] = projectTitle
    session["project_number"] = projectNumber
    session['project_icon'] = "default.svg"
    # ペルソナはデフォルトで未定義にする
    session['persona_number'] = None
    session['sprint'] = 1
    return redirect("/create_stories")

# テンプレートから作成する
@apple.route('/create_project2')
@login_required
def create_project2():
    return render_template('/project/createproject2.html')

@apple.route('/action/create_project2', methods=['POST'])
@login_required
def create_template():
    if request.method == 'POST':
        title = request.form.get('title')
        target_class = request.form.get('target_class')
        team = int(request.form.get('team'))
        sorting = request.form.get('gen')
        coma = int(request.form.get('coma'))
        sharedFolderInput = request.form.get('sharedFolderInput')
        owner_name = str(session.get("user_name"))
        owner_email = str(session.get("user_id"))
        
        cur = mysql.get_db().cursor()
        
        cur.execute("SELECT userNumber FROM student WHERE class = (%s)", (target_class,))
        userNumber = cur.fetchall()
        
        # タプルからリストに変換
        userNumber = list(userNumber)
        
        # 指定されたチーム数から、チームごとの人数を計算
        number_of_team = int(len(userNumber) / team)
        count = 0
        # チームへ割り振りが完了したユーザーのリスト
        endUserNumber = []
        
        if sorting == "random":
            # ランダムにユーザーを割り振る
            random.shuffle(userNumber)
        for i in range(0, team):
            cur.execute("INSERT INTO project(name, owner, start_date, finish_date, googleDrive) VALUES (%s, %s, %s, %s, %s)", (title + '_チーム' + str(i+1), owner_name, "2020-01-01", "2020-01-01", sharedFolderInput))
            mysql.get_db().commit()
            projectId = cur.lastrowid
            # プロジェクトオーナーに作成した先生を追加
            cur.execute("INSERT INTO project_users(projectName, userId, projectNumber) VALUES (%s, %s, %s)", (title + '_チーム' + str(i+1), owner_email, projectId))
            
            # チームごとの人数分だけユーザーを割り振る
            for j in range(0, number_of_team):
                user = userNumber[count][0]
                cur.execute("SELECT userId FROM users WHERE userNumber = (%s)", (user,))
                uid = cur.fetchone()
                cur.execute("INSERT INTO project_users(projectName, userId, projectNumber) VALUES (%s, %s, %s)", (title + '_チーム' + str(i+1), uid, projectId))
                mysql.get_db().commit()
                count += 1
            # チームごとの人数が割り振り終わった後、残りの人数を割り振る
            if i < (len(userNumber) % team):
                user = userNumber[count][0]
                cur.execute("SELECT userId FROM users WHERE userNumber = (%s)", (user,))
                uid = cur.fetchone()
                cur.execute("INSERT INTO project_users(projectName, userId, projectNumber) VALUES (%s, %s, %s)", (title + '_チーム' + str(i+1), uid, projectId))
                mysql.get_db().commit()
                endUserNumber.append(userNumber[count][0])
                count += 1
        return redirect("/select_project")
    else:
        return "render_template('/project/createproject2.html')"

@apple.route('/create_project99')
def create_project99():
    cur = mysql.get_db().cursor()
    for i in range(0, 100):
        cur.execute("INSERT INTO users(userId, userName, kana, password, gender, class) VALUES (%s, %s, %s, %s, %s, %s)", ("test" + str(i) + "@st.jp", "テストアカウント" + str(i), "テストアカウント" + str(i), "scrypt:32768:8:1$L2mjfpTmVhyNbN2q$5bf4d6b94f85e10c3fa9a63adddecdd9c2cb919162164bdea0713af1da5fd042578115b0759fd2a1812ff970b6da4318ee3fd369ef5e3e4afa0791ea13948d75", 0, "student"))
        mysql.get_db().commit()
        cur.execute("INSERT INTO achievement(userNumber) VALUES (%s)", (i + 11))
        mysql.get_db().commit()
        if i < 25:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 11, "kd1290" + str(i), "0J01", "0J010" + str(i)))
            mysql.get_db().commit()
        elif i < 50:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 11, "kd1290" + str(i), "0J02", "0J020" + str(i)))
            mysql.get_db().commit()
        elif i < 75:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 11, "kd1290" + str(i), "0J03", "0J030" + str(i)))
            mysql.get_db().commit()
        else:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 11, "kd1290" + str(i), "0J04", "0J040" + str(i)))
            mysql.get_db().commit()
    cur.close()
    return "DB Insert Complete!"