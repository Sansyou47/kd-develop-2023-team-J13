from flask import Blueprint, render_template, request, redirect, session ,url_for
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

story = Blueprint("story", __name__)

mysql = None

@story.route("/create_stories", methods=["GET", "POST"])  # ストーリー追加、表示処理
@login_required
def storeis():
    stories = None
    priority = None
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
        return redirect(url_for('story.storeis'))  # POST後にリダイレクト
    # 共通の処理（GETメソッドでの処理）
    cur.execute("SELECT name FROM story WHERE projectNumber = %s", projectNumber)
    story_data = cur.fetchall()
    if story_data:
        session.pop("backlog", None)
        session["backlog"] = story_data
    # ペルソナの情報を取得
    cur.execute("SELECT * FROM persona WHERE projectNumber = %s", (session.get("project_number")))
    persona = cur.fetchone()
    session["persona"] = persona
    cur.execute("SELECT name FROM task WHERE projectNumber = %s", (projectNumber))
    taskName = cur.fetchall()
    session["taskName"] = taskName
    cur.close()
    conn.close()
    return render_template("stories/create_stories.html", project=projectNumber, persona=persona, taskName = taskName)
    
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

@story.route('/action/register_persona', methods=['POST'])
@login_required
def register_persona():
    persona = []
    if request.method == "POST":
        persona.append(session.get("project_number"))
        persona.append(request.form.get('name'))
        persona.append(int(request.form.get('age')))
        gender = request.form.get('gender')
        if gender is not None:
            if gender == 'men':
                persona.append(0)
            else:
                persona.append(1)
        persona.append(request.form.get('job'))
        persona.append(request.form.get('hobby'))
        persona.append(int(request.form.get('income')))
        persona.append(request.form.get('family'))
        persona.append(request.form.get('note'))
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM persona WHERE projectNumber = %s", (session.get("project_number")))
        # テーブルにデータがある場合は更新、ない場合は追加
        if cur.fetchone():
            cur.execute("UPDATE persona SET name = %s, age = %s, gender = %s, job = %s, hobby = %s, income = %s, family = %s, note = %s WHERE projectNumber = %s", (persona[1], persona[2], persona[3], persona[4], persona[5], persona[6], persona[7], persona[8], persona[0]))
            conn.commit()
        else:
            cur.execute("INSERT INTO persona(projectNumber, name, age, gender, job, hobby, income, family, note) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (persona[0], persona[1], persona[2], persona[3], persona[4], persona[5], persona[6], persona[7], persona[8]))
            conn.commit()
        cur.close()
        conn.close()
        
    return render_template("stories/create_stories.html", project=session.get("project_number"), persona=persona, taskName=session.get("taskName"))