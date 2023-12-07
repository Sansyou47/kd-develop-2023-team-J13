from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

story = Blueprint("story", __name__)

mysql = None

@story.route("/create_stories", methods=["GET", "POST"])  # ストーリー追加、表示処理
def storeis():
    project = str(session.get("project"))
    conn = mysql.get_db()
    cur = conn.cursor()
    if request.method == "POST":
        # POSTメソッドでの処理
        stories = request.form.get("stories")
        # projectの追加が必要
        cur.execute("INSERT INTO story(name,project) VALUES(%s,%s)", (stories, project))
        conn.commit()
    # 共通の処理（GETメソッドでの処理）
    cur.execute("SELECT name FROM story WHERE project = %s", project)
    story_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("stories/create_stories.html", story_data=story_data, project=project
    )
    
# ストーリー選択画面
@story.route("/choice_story")
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
