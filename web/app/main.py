from flask import Flask, render_template, request, redirect
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
    return render_template("/task.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
