from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required, current_user

delete = Blueprint("delete", __name__)

mysql = None

@delete.route("/delete_data")
@login_required
def delete_data():
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
            taskName += ('0',)
        else :
            cur.execute("SELECT name FROM task WHERE story = %s", (storyName[i]))
            taskName += cur.fetchall()
    

    conn.commit()
    cur.close()
    return render_template("/delete/delete_data.html", projectName = projectName, storyName = storyName, taskName = taskName)