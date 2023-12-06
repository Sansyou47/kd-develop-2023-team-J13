from flask import Flask, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask import jsonify
from function import select_project, task, indexp, story
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

select_project.mysql = mysql
task.mysql = mysql
story.mysql = mysql

app.register_blueprint(select_project.select_project)
app.register_blueprint(task.task)
app.register_blueprint(indexp.indexp)

app.secret_key = 'your_secret_key'

# セッションに値を格納
@app.route('/set_session')
def set_session():
    # getメソッドで取得した値をセッションに格納
    project = request.args.get('project')
    session['project'] = project
    # とりあえずインデックスへリダイレクト
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')