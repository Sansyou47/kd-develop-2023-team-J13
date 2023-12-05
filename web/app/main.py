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
    #テストのため一時的に変更
    return redirect('/create_stories')

@app.route('/')
def index():
    data=str(session.get('project'))
    return data

@app.route('/project')
def project():
    return render_template('select_project.html')

@app.route('/create_stories', methods=['GET', 'POST'])#ストーリー追加、表示処理
def storeis():
    project=str(session.get('project'))
    conn = mysql.get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        # POSTメソッドでの処理
        stories = request.form.get('stories')
        #projectの追加が必要
        cur.execute("INSERT INTO story(name,project) VALUES(%s,%s)", (stories,project))
        conn.commit()
    # 共通の処理（GETメソッドでの処理）
    cur.execute("SELECT name FROM story WHERE project = %s",project)
    story_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('stories/create_stories.html', story_data=story_data,project=project)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')