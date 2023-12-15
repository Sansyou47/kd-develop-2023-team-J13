from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

init_session = Blueprint("init_session", __name__)

mysql = None

# セッションに値を格納
@init_session.route("/set_session")
def set_session():
    # sessionを初期化
    session.pop('project_users', None)
    project = request.args.get("project")
    cur = mysql.get_db().cursor()
    cur.execute("SELECT userId FROM project_users WHERE projectName = %s", (project))
    userId = cur.fetchall()
    uName = []
    for userid in userId:
        cur.execute("SELECT userName FROM users WHERE userId = %s", (userid[0],))
        userName = cur.fetchall()
        if userName:
            uName.append(userName[0])
    
    session['project_users'] = uName
    session["project"] = project
    # テストのため一時的に変更
    return redirect("/create_stories")