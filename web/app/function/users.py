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
        # MySQLへ接続
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE userId = %s", (userid,))
        user = cur.fetchone()
        # メールアドレスが使用済みの場合
        if user:
            error_message = "このメールアドレスは既に使用されています。"
            return render_template("register.html", email=userid, name=name, kana=kana, error_message=error_message)
        # パスワードが8文字未満の場合
        elif len(password) < 8:
            error_message = "メールアドレスは8文字以上で入力してください。"
            return render_template("register.html", email=userid, name=name, kana=kana, error_message=error_message)
        else:
            # パスワードをハッシュ化
            hashed_password = generate_password_hash(password)
            # SQL実行
            cur.execute("INSERT INTO users(userId, userName, kana, password) VALUES(%s,%s,%s,%s)", (userid, name, kana, hashed_password))
            conn.commit()
            cur.close()
            conn.close()
            return redirect("/login")
    # POSTメソッドに値が渡されていない場合、登録画面へ遷移
    else:
        return render_template("register.html")
    