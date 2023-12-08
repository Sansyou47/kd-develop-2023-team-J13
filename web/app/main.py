from flask import Flask, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL
from flask import jsonify
from function import story, project, task, init_session, apple, graph
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config["MYSQL_DATABASE_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_DATABASE_HOST"] = "mysql"

mysql = MySQL(app)

app.register_blueprint(story.story)
app.register_blueprint(project.project)
app.register_blueprint(task.task)
app.register_blueprint(init_session.init_session)
app.register_blueprint(apple.apple)
app.register_blueprint(graph.graph)

story.mysql = mysql
project.mysql = mysql
task.mysql = mysql
init_session.mysql = mysql
apple.mysql = mysql

app.secret_key = "your_secret_key"

@app.route("/")
def index():
    data = str(session.get("project"))
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
