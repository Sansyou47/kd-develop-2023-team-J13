from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

story = Blueprint("story", __name__)

mysql = None

@story.route("/create_stories", methods=["GET", "POST"])  # ストーリー追加、表示処理
@login_required
def storeis():
    projectNumber = str(session.get("project_number"))
    conn = mysql.get_db()
    cur = conn.cursor()
    if request.method == "POST":
        # POSTメソッドでの処理
        stories = request.form.get("stories")
        priority = request.form.get("priority")
        # projectの追加が必要
        cur.execute("INSERT INTO story(name,projectNumber,priorit) VALUES(%s,%s,%s)", (stories, projectNumber,priority))
        conn.commit()
    # 共通の処理（GETメソッドでの処理）
    cur.execute("SELECT name FROM story WHERE projectNumber = %s", projectNumber)
    story_data = cur.fetchall()
    if story_data:
        session.pop("backlog", None)
        session["backlog"] = story_data
    # ペルソナの情報を取得
    cur.execute("SELECT personaNumber FROM project WHERE projectNumber = %s", projectNumber)
    tmp = cur.fetchone()
    persona = []
    if tmp:
        cur.execute("SELECT * FROM persona WHERE personaNumber = %s", tmp[0])
        persona = cur.fetchone()
    cur.close()
    conn.close()
    return render_template("stories/create_stories.html", project=projectNumber, persona=persona)
    
    
# ストーリー選択画面
@story.route("/choice_story")
@login_required
def choice_story():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT * FROM story")
    storyData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template("/tasks/choice_story.html", storyData=storyData)
