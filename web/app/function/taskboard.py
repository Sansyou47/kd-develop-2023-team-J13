from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required

taskboard = Blueprint("taskboard", __name__)
mysql = None

def get_story_and_tasks(projectNumber, sprint):
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    # ストーリーの名前を取得
    cur.execute("SELECT name FROM story WHERE  projectNumber = %s AND sprint = %s", (projectNumber, sprint))
    Story = cur.fetchall()

    # タスクの名前とステータスを取得(他人のコードいじるの怖いので*はこのままで)
    all_tasks = []
    cur.execute("SELECT * FROM task WHERE  projectNumber = %s AND sprint = %s", (projectNumber, session.get("now_sprint")))
    tasks_for_story = cur.fetchall()
    all_tasks.extend(tasks_for_story)

    conn.commit()
    cur.close()

    return Story, all_tasks  # Storyとall_tasksを返す

@taskboard.route("/taskboard", methods=["GET","POST"])
def outtaskboard():
    projectNumber = str(session.get("project_number"))
    Story, all_tasks = get_story_and_tasks(projectNumber, session.get("now_sprint"))  # get_story_and_tasksからStoryとall_tasksを受け取る
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

    return '', 200  # HTTPステータスコード200（成功）を返す


@taskboard.route("/action/changetaskboard_sprint", methods=["GET"])
@login_required
def change_sprint():
    sprint = int(request.args.get("ppp"))
    session["now_sprint"] = sprint
    projectNumber = str(session.get("project_number"))
    Story, all_tasks = get_story_and_tasks(projectNumber, session.get("now_sprint"))  # get_story_and_tasksからStoryとall_tasksを受け取る
    return render_template("/taskboard.html", story=Story,task=all_tasks)
