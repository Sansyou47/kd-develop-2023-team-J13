from flask import Blueprint, request, render_template
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
        cur.execute("SELECT * FROM project WHERE name = %s", (project_name[0],))
        project_data = cur.fetchall()
        if project_data:
            data.append(project_data[0])

    return render_template('/select_project.html', data=data)

# プロジェクトを選択したときの処理
@select_project.route('/action/select_project',methods=['POST'])
@login_required
def select_project_action():
    project = request.form.get('project')
    return str(project)