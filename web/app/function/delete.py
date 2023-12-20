from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

delete = Blueprint("delete", __name__)

mysql = None

@delete.route("/delete_data")
@login_required
def delete_data():
    projectNumber = str(session.get("project_number"))
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
