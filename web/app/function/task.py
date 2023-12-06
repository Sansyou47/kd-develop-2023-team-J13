from flask import Blueprint, request, render_template, redirect, session
from flaskext.mysql import MySQL

task=Blueprint('task',__name__)

mysql=None

# task追加画面
@task.route('/add_task', methods=['POST'])
def add_task():
    storyName = request.form.get('storyName')
    projectName = request.form.get('projectName')
    return render_template('/tasks/add_task.html', storyName = storyName, projectName = projectName)

#task追加アクション
@task.route('/action/add_task', methods=['POST'])
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
    
@task.route('/get_task')
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

