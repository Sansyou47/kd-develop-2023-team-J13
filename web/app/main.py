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

@app.route('/')
def index():
    data=str(session.get('project'))
    return data

@app.route('/create_project')
def create_project():
    return render_template('/project/createproject.html')

@app.route('/create_project1')
def create_project1():
    return render_template('/project/createproject1.html')

@app.route('/action/create_project1', methods=['POST'])
def action_create_project1():

    conn = mysql.get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        # POSTメソッドでの処理
        projectTitle = request.form.get('projectTitle')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        collaborator = request.form.get('collaborator')
        urlInput = request.form.get('urlInput')
        sharedFolderInput = request.form.get('sharedFolderInput')
        #projectの追加が必要
        cur.execute("INSERT INTO project(name,start_date,update_date,owner,github,googleDrive) VALUES(%s,%s,%s,%s,%s,%s)", (projectTitle,startDate,endDate,collaborator,urlInput,sharedFolderInput))
        conn.commit()
    cur.close()
    conn.close()


    return redirect('/select_project')


@app.route('/create_project2')
def create_project2():
    return render_template('/project/createproject2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')