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
@apple.route('/create_project2')
def create_project2():
    return render_template('/project/createproject2.html')
