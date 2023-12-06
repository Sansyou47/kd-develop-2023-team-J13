from flask import Blueprint, request, render_template
from flaskext.mysql import MySQL

select_project = Blueprint('select_project', __name__)

mysql = None  # MySQLオブジェクトを保持するための変数

@select_project.route('/select_project')
def my_route():
    # MySQLへ接続
    cur = mysql.get_db().cursor()
    # SQL実行
    cur.execute("SELECT * FROM project")
    data = cur.fetchall()
    return render_template('/select_project.html', data=data)

@select_project.route('/action/select_project',methods=['POST'])
def select_project_action():
    project = request.form.get('project')
    return str(project)