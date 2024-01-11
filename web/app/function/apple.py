from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required

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

        # プロジェクト情報を保存
        cur.execute("INSERT INTO project(name, owner, start_date, finish_date, github, googleDrive) VALUES (%s, %s, %s, %s, %s, %s)", (projectTitle, uName, startDate, endDate, urlInput, sharedFolderInput))
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
    return redirect("/create_stories")

# テンプレートから作成する
@apple.route('/create_project2', methods=['POST'])
def create_project2():
    if request.method == 'POST':
        title = request.form.get('title')
        target_class = request.form.get('class')
        team = int(request.form.get('team'))
        coma = int(request.form.get('coma'))
        sharedFolderInput = request.form.get('sharedFolderInput')
        
        
        return render_template('/project/createproject2.html')
    else:
        return render_template('/project/createproject2.html')

@apple.route('/create_project99')
def create_project99():
    cur = mysql.get_db().cursor()
    for i in range(0, 100):
        cur.execute("INSERT INTO users(userId, userName, kana, password, gender, class) VALUES (%s, %s, %s, %s, %s, %s)", ("test" + str(i) + "@st.jp", "テストアカウント" + str(i), "テストアカウント" + str(i), "scrypt:32768:8:1$L2mjfpTmVhyNbN2q$5bf4d6b94f85e10c3fa9a63adddecdd9c2cb919162164bdea0713af1da5fd042578115b0759fd2a1812ff970b6da4318ee3fd369ef5e3e4afa0791ea13948d75", 0, "student"))
        mysql.get_db().commit()
        cur.execute("INSERT INTO achievement(userNumber) VALUES (%s)", (i + 10))
        mysql.get_db().commit()
        if i < 25:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 10, "kd1290" + str(i), "0J01", "0J010" + str(i)))
            mysql.get_db().commit()
        elif i < 50:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 10, "kd1290" + str(i), "0J02", "0J020" + str(i)))
            mysql.get_db().commit()
        elif i < 75:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 10, "kd1290" + str(i), "0J03", "0J030" + str(i)))
            mysql.get_db().commit()
        else:
            cur.execute("INSERT INTO student(userNumber, studentNumber, class, number) VALUES (%s, %s, %s, %s)", (i + 10, "kd1290" + str(i), "0J04", "0J040" + str(i)))
            mysql.get_db().commit()
    cur.close()
    return "DB Insert Complete!"