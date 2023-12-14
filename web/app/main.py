from flask import Flask, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from function import story, select_project, task, init_session, apple, mypage, graph, users
from werkzeug.security import check_password_hash
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
app.register_blueprint(select_project.select_project)
app.register_blueprint(task.task)
app.register_blueprint(init_session.init_session)
app.register_blueprint(apple.apple)
app.register_blueprint(mypage.mypage)
app.register_blueprint(graph.graph)
app.register_blueprint(users.users)

story.mysql = mysql
select_project.mysql = mysql
task.mysql = mysql
init_session.mysql = mysql
apple.mysql = mysql
mypage.mysql = mysql
graph.mysql = mysql
users.mysql = mysql

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        
# ログイン中のユーザーIDを取得する関数
def get_uid():
    # ユーザーIDを取得し、戻り値に設定する（メアドから"@"以降を削除する処理を追加）
    uid = str(current_user.id)
    uid = uid.split('@')[0]
    return uid


@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s", (user_id))
    user = cursor.fetchone()
    if user:
        return User(user_id)
    else:
        return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userid = request.form["userid"]
        password = request.form["password"]
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM users WHERE userId = %s", (userid))
        user = cursor.fetchone()
        
        # パスワードをハッシュ値と照合して一致した場合
        if user and check_password_hash(user[4], password):
            login_user(User(userid))
            uid = str(current_user.id)
            uid = uid.split('@')[0]
            session['user_id'] = uid
            return redirect('/select_project')
        else:
            error_message = "ユーザーIDまたはパスワードが間違っています。"
            return render_template('login.html', error_message=error_message)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('user_id', None)
    return redirect("/login")


@app.route("/auth")
@login_required
def auth():
    user_id = current_user.id
    return user_id


@app.route("/")
@login_required
def index():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
