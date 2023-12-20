from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

init_session = Blueprint("init_session", __name__)

mysql = None

# セッションに値を格納
@init_session.route("/set_session")
def set_session():
    # sessionを初期化
    session.pop('project_users', None)
    project_number = int(request.args.get("project_number"))
    cur = mysql.get_db().cursor()
    cur.execute("SELECT name, github, googleDrive, logo FROM project WHERE projectNumber = %s", (project_number))
    data = cur.fetchone()
    cur.execute("SELECT userId FROM project_users WHERE projectNumber = %s", (project_number))
    userId = cur.fetchall()
    uName = []
    for userid in userId:
        cur.execute("SELECT userName FROM users WHERE userId = %s", (userid[0]))
        userName = cur.fetchall()
        if userName:
            uName.append(userName[0])
    if data[3] == None:
        session['project_icon'] = "default.svg"
    else:
        session['project_icon'] = data[3]
    session['project_github'] = data[1]
    session['project_googleDrive'] = data[2]
    session['project_users'] = uName
    session["project"] = data[0]
    session["project_number"] = project_number
    # テストのため一時的に変更
    return redirect("/create_stories")