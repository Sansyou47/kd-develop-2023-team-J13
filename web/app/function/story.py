from flask import Blueprint, render_template, request
from flaskext.mysql import MySQL

story = Blueprint('story', __name__)

mysql=None

story.route('/create_storeis')
def storeis():
    return render_template('/templates/stories/create_stories.html')

@story.route('/action/create_stories',methods=['POST'])
def add_stories():
    stories = request.form.get('stories')
    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    cur.execute("INSERT INTO employee(project_int,stories_name,stories) VALUES(%s,%s,%s)",(hoge,stories,hoge))
    conn.commit()
    cur.close()
    return render_template('/templates/stories/create_stories.html')

# ストーリー選択画面
@story.route('/choice_story')
def choice_story():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT * FROM story")
    storyData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template('/tasks/choice_story.html', storyData = storyData)