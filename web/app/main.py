from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import test
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

app.register_blueprint(test.app)

@app.route('/')
def index():
    return 'Test'

@app.route('/create_storeis')
def storeis():  
    return render_template('/templates/stories/create_stories.html')

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

# task追加画面
@app.route('/add_task', methods=['POST'])
def add_task():
    storyName = request.form.get('storyName')
    projectName = request.form.get('projectName')
    return render_template('/tasks/add_task.html', storyName = storyName, projectName = projectName)

@app.route('/action/add_task', methods=['POST'])
def action_add_task():
    taskName = request.form.get('taskName')
    taskManager = request.form.get('taskManager')
    sprint = int(request.form.get('sprint'))
    projectName = request.form.get('projectName')

    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    cur.execute("INSERT INTO task(name, manager, project, sprint) VALUES(%s, %s ,%s ,%s)",(taskName, taskManager, projectName, sprint))
    conn.commit()
    cur.close()

    return get_task()
    #return render_template('/choice_story')

# ストーリー選択画面
@app.route('/choice_story')
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

@app.route('/get_task')
def get_task():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT * FROM task")
    taskData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template('/tasks/get_task.html', taskData = taskData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')