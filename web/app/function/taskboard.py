from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

taskboard = Blueprint("taskboard", __name__)

mysql = None
@taskboard.route("/taskboard", methods=["GET","POST"])
def outtaskboard():
    project = str(session.get("project"))
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT name FROM story WHERE project = %s",project)
    Story = cur.fetchall()

    all_tasks = []

    for row in Story:
        cur.execute("SELECT * FROM task WHERE story = %s",row)
        tasks_for_story = cur.fetchall()
        all_tasks.extend(tasks_for_story)

    conn.commit()
    cur.close()

    return render_template("/taskboard.html", story=Story,task=all_tasks)

# taskbordをDoingやDoneに移動させる
@taskboard.route("/taskboardjs", methods=["POST"])
def taskboardjs():
    conn = mysql.get_db()
    cur = conn.cursor()
    data = request.get_json()
    cur.execute(
        "UPDATE task SET status = %s WHERE name = %s ",
        (data['st'] ,data['taskname']),
    )

    conn.commit()
    cur.close()
