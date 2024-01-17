from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

delete = Blueprint("delete", __name__)

mysql = None

@delete.route("/delete_data")
@login_required
def delete_data():
    projectNumber = str(session.get("projectNumber"))
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    cur.execute("SELECT projectName FROM project_users WHERE userId = %s", (current_user.id))
    projectName = cur.fetchall()
    #空のタプル配列の宣言
    storyName = ()
    taskName = ()
    #プロジェクトネームの要素数分だけ繰り返す
    for i in range(len(projectName)):
        cur.execute("SELECT name FROM story WHERE project = %s", (projectName[i]))
        storyName += cur.fetchall()
        #区切りの為に0を入れる
        storyName += ('0',) #タプル宣言の為にコンマを入れる
    
    for i in range(len(storyName)):
        if storyName[i] == '0':
            pass
        else :
            cur.execute("SELECT name FROM task WHERE story = %s", (storyName[i]))
            taskName += cur.fetchall()
            taskName += ('1',)
    

    conn.commit()
    cur.close()
    lenProject = len(projectName)
    numStory = []
    numTask = []
    spanProject = []
    w1 = 0
    w2 = 0
    j = 0

    for i in range(len(taskName)):
        if taskName[i] == '1':
            numTask.append(w1)
            w1 = 0
        else:
            w1 += 1
    

    for i in range(len(storyName)):
        if storyName[i] == '0':
            numStory.append(w1)
            spanProject.append(w2)
            w1 = 0
            w2 = 0
        else:
            w1 += 1
            w2 += numTask[j]
            j += 1

    #作業用タプルを宣言
    w1t = ()
    w2t = ()

    #taskの配列から区切り文字'1'を排除
    for i in range(len(taskName)):
        if taskName[i] == '1':
            pass
        else:
            w1t += (taskName[i],)
    
    #storyの配列から区切り文字'0'を排除
    for i in range(len(storyName)):
        if storyName[i] == '0':
            pass
        else:
            w2t += (storyName[i],)
    
    #プロジェクト名タプルをリストに変換
    projectList = []
    for i in range(len(projectName)):
        projectList += projectName[i]

    #storyList = [w2t[i] for i in range(len(w2t))]
    #ストーリー名タプルをリストに変換
    storyList = []
    for i in range(len(w2t)):
        storyList += w2t[i]

    #タスク名タプルをリストに変換
    taskList = []
    for i in range(len(w1t)):
        taskList += w1t[i]
    
    #これはList内包表記 -> taskList = [i for sublist in w1t for i in sublist]

    return render_template("/delete/delete_data.html", projectName = projectList, storyName = storyList, taskName = taskList, lenProject = lenProject, numStory = numStory, numTask = numTask, spanProject = spanProject)


@delete.route("/action/delete_project", methods=["POST"])
@login_required
def delete_project():
    ok = request.form.get("ok")
    project_number = request.form.get("projectNumber")
    user_id = session['user_id']
    user_name = session['user_name']
    #ok 変数に値が入っているならDELETE処理実行
    if ok :
        # MySQLへ接続
        conn = mysql.get_db()
        cur = conn.cursor()

        cur.execute("SELECT owner FROM project WHERE projectNumber = %s", (project_number))
        
        project_owner = cur.fetchone()

        conn.commit()
        cur.close()


        if project_owner[0] == user_name: #プロジェクトのオーナとプロジェクト離脱者が同じならプロジェクトを削除する
            # MySQLへ接続
            conn = mysql.get_db()
            cur = conn.cursor()

            # SQL実行
            cur.execute("DELETE FROM task WHERE projectNumber = %s", (project_number))
            cur.execute("DELETE FROM story WHERE projectNumber = %s", (project_number))
            cur.execute("DELETE FROM project WHERE projectNumber = %s", (project_number))

            conn.commit()
            cur.close()
            
        else: #プロジェクトのオーナとプロジェクト離脱者が違うならプロジェクトから離脱する

            # MySQLへ接続
            conn = mysql.get_db()
            cur = conn.cursor()

            # SQL実行
            cur.execute("DELETE FROM project_users WHERE userId = %s AND projectNumber = %s", (user_id, project_number))

            conn.commit()
            cur.close()

    return redirect("/select_project")

@delete.route("/action/delete_story", methods=["POST"])
@login_required
def delete_story():
    ok = request.form.get("ok")
    story_name = request.form.get("story-name")
    project_number = session['project_number']
    #ok 変数に値が入っているならDELETE処理実行
    if ok :
        # MySQLへ接続
        conn = mysql.get_db()
        cur = conn.cursor()

        # SQL実行
        cur.execute("DELETE FROM task WHERE projectNumber = %s AND story = %s", (project_number, story_name))
        cur.execute("DELETE FROM story WHERE projectNumber = %s AND name = %s", (project_number, story_name))

        conn.commit()
        cur.close()
        

    return redirect("/create_stories")

@delete.route("/action/delete_task", methods=["POST"])
@login_required
def delete_task():
    ok = request.form.get("ok")
    task_name = request.form.get("task-name")
    project_number = session['project_number']
    #ok 変数に値が入っているならDELETE処理実行
    if ok :
        # MySQLへ接続
        conn = mysql.get_db()
        cur = conn.cursor()

        # SQL実行
        cur.execute("DELETE FROM task WHERE projectNumber = %s AND name = %s", (project_number, task_name))

        conn.commit()
        cur.close()
        

    return redirect("/create_stories")