from flask import Flask, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask import jsonify
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

app.secret_key = 'your_secret_key'

# セッションに値を格納
@app.route('/set_session')
def set_session():
    project = request.args.get('project')
    session['project'] = project
    return redirect('/select_project')

@app.route('/')
def index():
    data=str(session.get('project'))
    return data

@app.route('/project')
def project():
    return render_template('select_project.html')

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

@app.route('/select_project')
def select_project():
    # MySQLへ接続
    cur = mysql.get_db().cursor()
    # SQL実行
    cur.execute("SELECT * FROM project")
    data = cur.fetchall()
    return render_template('/select_project.html', data=data)

@app.route('/action/select_project',methods=['POST'])
def select_project_action():
    project = request.form.get('project')
    return str(project)

# task追加画面
@app.route('/add_task', methods=['POST'])
def add_task():
    storyName = request.form.get('storyName')
    projectName = request.form.get('projectName')
    return render_template('/tasks/add_task.html', storyName = storyName, projectName = projectName)

#task追加アクション
@app.route('/action/add_task', methods=['POST'])
def action_add_task():
    taskName = request.form.get('taskName')
    taskManager = request.form.get('taskManager')
    sprint = int(request.form.get('sprint'))
    storyName = request.form.get('storyName')

    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    cur.execute("INSERT INTO task(name, manager, story, sprint) VALUES(%s, %s ,%s ,%s)",(taskName, taskManager, storyName, sprint))
    conn.commit()
    cur.close()

    return  redirect('/get_task')
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