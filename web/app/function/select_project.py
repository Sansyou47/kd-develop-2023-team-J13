from flask import Blueprint, request, render_template, session
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

select_project = Blueprint('select_project', __name__)

mysql = None  # MySQLオブジェクトを保持するための変数

@select_project.route('/select_project')
@login_required
def my_route():
    # MySQLへ接続
    cur = mysql.get_db().cursor()
    # SQL実行
    cur.execute("SELECT projectName FROM project_users WHERE userId = %s", (current_user.id))
    project_names = cur.fetchall()
    data = []
    # 現在ログインしているユーザーが参加しているプロジェクトを取得
    for project_name in project_names:
        cur.execute("SELECT * FROM project WHERE name = %s", (project_name[0]))
        project_data = cur.fetchall()
        if project_data:
            data.append(project_data[0])

    return render_template('/select_project.html', data=data)

# プロジェクトを選択したときの処理
@select_project.route('/action/select_project',methods=['POST'])
@login_required
def select_project_action():
    project = request.form.get('project')
    cur = mysql.get_db().cursor()
    cur.execute("SELECT userId FROM project_users WHERE projectName = %s", ('開発支援アプリ'))
    userId = cur.fetchall()
    uName = []
    for userid in userId:
        cur.execute("SELECT userName FROM users WHERE userId = %s", (userid[0],))
        userName = cur.fetchall()
        if userName:
            uName.append(userName[0])
    
    session['project_users'] = 'uName'
    return str(project)