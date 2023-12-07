from flask import Blueprint, render_template, request
from flaskext.mysql import MySQL

project = Blueprint("project", __name__)

mysql = None

@project.route("/project")
def project_page():
    return render_template("select_project.html")

@project.route("/select_project")
def select_project():
    # MySQLへ接続
    cur = mysql.get_db().cursor()
    # SQL実行
    cur.execute("SELECT * FROM project")
    data = cur.fetchall()
    return render_template("/select_project.html", data=data)

@project.route("/action/select_project", methods=["POST"])
def select_project_action():
    project = request.form.get("project")
    return str(project)