from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash
from flask_login import current_user

users = Blueprint("users", __name__)

mysql = None

@users.route("/register", methods=["GET", "POST"])
def register():
    error_message = None
    if request.method == "POST":
        # POSTメソッドでの処理
        userid = request.form.get("userId")
        password = request.form.get("password")
        name = request.form.get("name")
        kana = request.form.get("kana")
        
        # パスワードをハッシュ化
        hashed_password = generate_password_hash(password)
        
        # MySQLへ接続
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE userId = %s", (userid,))
        user = cur.fetchone()
        # メールアドレスが使用済みの場合
        if user:
            error_message = "このユーザーIDは既に使用されています。"
            return render_template("register.html", error_message=error_message)
        else:
            # SQL実行
            cur.execute("INSERT INTO users(userId, userName, kana, password) VALUES(%s,%s,%s,%s)", (userid, name, kana, hashed_password))
            conn.commit()
            cur.close()
            conn.close()
            return redirect("/login")
    # POSTメソッドに値が渡されていない場合、登録画面へ遷移
    else:
        return render_template("register.html")
    