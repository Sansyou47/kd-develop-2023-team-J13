from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test'

@app.route('/action/create_stories',methods=['POST'])
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