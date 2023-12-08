from flask import Flask, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask import jsonify
from function import story, project, task, init_session, apple
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config["MYSQL_DATABASE_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_DATABASE_HOST"] = "mysql"

app.secret_key = os.getenv("SECRET_KEY")

mysql = MySQL(app)

app.register_blueprint(story.story)
app.register_blueprint(project.project)
app.register_blueprint(task.task)
app.register_blueprint(init_session.init_session)
app.register_blueprint(apple.apple)

story.mysql = mysql
project.mysql = mysql
task.mysql = mysql
init_session.mysql = mysql
apple.mysql = mysql

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM users WHERE userId = %s', (user_id))
    user = cursor.fetchone()
    if user:
        return User(user_id)
    else:
        return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM users WHERE userId = %s', (userid))
        user = cursor.fetchone()
        if user and password == user[4]:
            return redirect('/select_project')
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return 'Logged in as: ' + current_user.id

# @app.route("/")
# def index():
#     data = str(session.get("project"))
#     return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
