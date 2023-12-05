from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from function import test
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config["MYSQL_DATABASE_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_DATABASE_HOST"] = "mysql"

mysql = MySQL(app)

app.register_blueprint(test.app)


@app.route("/")
def index():
    return "Test"


@app.route("/task_task")
def task():
    # データベースからタスク一覧を取得
    connection = mysql.get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    return render_template("/templates/task_catch/task_catch.html", tasks=tasks)


@app.route("/change_status/<int:task_id>")
def change_status(task_id):
    # データベースから対象のタスクを取得
    connection = mysql.get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM task WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    # タスクのステータスを変更
    new_status = 1 if task["status"] == 0 else 0

    # データベースに変更を保存
    cursor.execute("UPDATE task SET status = %s WHERE id = %s", (new_status, task_id))
    connection.commit()

    return redirect(url_for("task"))


@app.route("/action/create_stories", methods=["POST"])
def add_stories():
    stories = request.form.get("stories")
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute(
        "INSERT INTO employee(project_int,stories_name,stories) VALUES(%s,%s,%s)",
        (hoge, stories, hoge),
    )
    conn.commit()
    cur.close()
    return render_template("/templates/stories/create_stories.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
