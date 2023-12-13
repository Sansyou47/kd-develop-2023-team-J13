from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

task = Blueprint("task", __name__)

mysql = None


# task追加画面
@task.route("/add_task", methods=["POST"])
def add_task():
    storyName = request.form.get("storyName")
    projectName = request.form.get("projectName")
    return render_template(
        "/tasks/add_task.html", storyName=storyName, projectName=projectName
    )


# task追加アクション
@task.route("/action/add_task", methods=["POST"])
def action_add_task():
    taskName = request.form.get("taskName")
    taskManager = request.form.get("taskManager")
    sprint = int(request.form.get("sprint"))
    storyName = request.form.get("storyName")
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute(
        "INSERT INTO task(name, manager, story, sprint) VALUES(%s, %s ,%s ,%s)",
        (taskName, taskManager, storyName, sprint),
    )
    conn.commit()
    cur.close()
    return redirect("/get_task")


@task.route("/get_task")
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


@task.route("/update_status", methods=["POST"])
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
        "UPDATE task SET status = %s ,manager = %s WHERE name = %s AND start_task_date = %s AND finish_task_date = %s",
        (task_status, task_users, task_name, start_date, finish_date),
    )
    conn.commit()
    cur.close()
    return redirect("/task_catch")


@task.route("/task_catch", methods=["GET"])
def task_catch():
    # project = str(session.get("project")) セッションを受け取れるようになったら(画面遷移が決まったら)コメントアウトを外しsql文を修正する
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    # namesの取得
    cur.execute("SELECT name FROM task")
    names = [item[0] for item in cur.fetchall()]

    # usersの取得
    cur.execute(
        "SELECT users.userName FROM users INNER JOIN project_users ON users.userId = project_users.userId WHERE project_users.projectName = '開発支援アプリ'"
    )
    users = [item[0] for item in cur.fetchall()]

    cur.close()
    return render_template("/task_catch/task_catch.html", names=names, users=users)
