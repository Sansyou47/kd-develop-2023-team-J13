from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required

apple = Blueprint("apple", __name__)

mysql = None

@apple.route('/create_project')
@login_required
def create_project():
    return render_template('/project/createproject.html')

# 新しいプロジェクトを作成する
@apple.route('/create_project1')
@login_required
def create_project1():
    return render_template('/project/createproject1.html', user_id=session['user_id'])

@apple.route('/action/create_project1', methods=['POST'])
@login_required
def action_create_project1():

    conn = mysql.get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        # POSTメソッドでの処理
        projectTitle = request.form.get('projectTitle')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        collaborator = request.form.get('collaborator')
        urlInput = request.form.get('urlInput')
        sharedFolderInput = request.form.get('sharedFolderInput')
        #projectの追加が必要
        cur.execute("INSERT INTO project(name,start_date,update_date,owner,github,googleDrive) VALUES(%s,%s,%s,%s,%s,%s)", (projectTitle,startDate,endDate,collaborator,urlInput,sharedFolderInput))
        conn.commit()
    cur.close()
    conn.close()


    return redirect('/select_project')

# テンプレートから作成する
@apple.route('/create_project2')
def create_project2():
    return render_template('/project/createproject2.html')

