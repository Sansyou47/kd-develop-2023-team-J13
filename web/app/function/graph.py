from flask import Blueprint, render_template, request, redirect, session
from flask_login import login_required
from flaskext.mysql import MySQL
import json

graph = Blueprint("graph", __name__)

mysql = None

@graph.route("/graph")
@login_required
def graphs():
    projectNumber = str(session.get("project_number"))
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT name FROM project WHERE projectNumber = %s",projectNumber)
    project = cur.fetchall()
    # SQL実行
    cur.execute("SELECT * FROM task WHERE projectNumber = %s",projectNumber)
    story_graph = cur.fetchall()

    conn.commit()
    cur.close()
    # story_graphを取得するコード
    return render_template('graph.html',story_graph = story_graph,project=project)