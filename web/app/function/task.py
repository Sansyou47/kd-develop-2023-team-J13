from flask import Blueprint, render_template, request, redirect, session
from flask_login import login_required
from flaskext.mysql import MySQL
from datetime import timedelta

task = Blueprint("task", __name__)

mysql = None


# task追加画面
@task.route("/add_task", methods=["POST"])
@login_required
def add_task():
    storyName = request.form.get("storyName")

    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    
    projectName = session.get("project")

    conn.commit()
    cur.close()
    #projectName = request.form.get("projectName")
    return render_template(
        "/tasks/add_task.html", storyName=storyName, projectName=projectName
    )


# task追加アクション
@task.route("/action/add_task", methods=["POST"])
@login_required
def action_add_task():
    taskName = request.form.get("taskName")
    sprint = int(session.get("now_sprint"))
    storyName = request.form.get("storyName")
    projectNumber = str(session.get("project_number"))
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT start_date FROM project WHERE projectNumber = %s", (projectNumber))
    Stert_date = cur.fetchone()[0]  # fetchone()を使って一つの値を取得
    delta_days = (sprint - 1) * 7
    stert_day = Stert_date + timedelta(days=delta_days)
    end_day = stert_day + timedelta(days=6)
    # SQL実行
    cur.execute(
        "INSERT INTO task(name, story, start_task_date, finish_task_date, sprint, projectNumber) VALUES(%s, %s ,%s ,%s,%s,%s)",
        (taskName, storyName, stert_day, end_day, sprint, projectNumber)
    )
    conn.commit()
    cur.close()

    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT name FROM task WHERE projectNumber = %s AND sprint = %s", (projectNumber, session.get("now_sprint")))
    taskName = cur.fetchall()

    conn.commit()
    cur.close()
    return render_template("stories/create_stories.html", project=projectNumber, taskName=taskName, persona=session.get("persona"))
    #return redirect("/report_task")

# タスク一覧取得
@task.route("/get_task")
@login_required
def get_task():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT * FROM task")
    taskData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template("/tasks/get_task.html", taskData=taskData)

#タスク状況報告画面
@task.route("/report_task")
@login_required
def report_task():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT * FROM task")
    taskData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template("/tasks/report_task.html", taskData=taskData)

@task.route("/report", methods=["POST"])
@login_required
def report():
    taskName = request.form.get("taskName")
    return render_template("/tasks/report.html", taskName=taskName)

@task.route("/action/report", methods=["POST"])
@login_required
def action_report():
    report = request.form.get("report")
    taskName = request.form.get("taskName")

    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("UPDATE task SET comment = %s WHERE name = %s", (report, taskName))

    conn.commit()
    cur.close()

    return redirect("/report_task")


@task.route("/update_status", methods=["POST"])
@login_required
def update_status():
    task_name = request.form["name"]
    task_status = request.form["status"]
    task_users = request.form["users"]
    start_date = request.form.get('start_date')
    finish_date = request.form.get('finish_date')
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE task SET status = %s ,manager = %s ,start_task_date = %s, finish_task_date = %s WHERE name = %s ",
        (task_status, task_users, start_date, finish_date, task_name),
    )
    conn.commit()
    cur.close()
    return redirect("/task_catch")


@task.route("/task_catch", methods=["GET"])
@login_required
def task_catch():
    project = str(session.get("project"))
    projectNumber = str(session.get("project_number"))
    conn = mysql.get_db()
    cur = conn.cursor()

    # namesの取得
    cur.execute(
        "SELECT name FROM task WHERE projectNumber = %s",(projectNumber,)
    )
    names = [item[0] for item in cur.fetchall()]

    # usersの取得
    cur.execute(
        "SELECT users.userName FROM users INNER JOIN project_users ON users.userId = project_users.userId WHERE project_users.projectNumber = %s",(projectNumber,)
    )
    users = [item[0] for item in cur.fetchall()]

    cur.close()
    return render_template("/task_catch/task_catch.html", names=names, users=users, projectNumber=projectNumber, project=project)