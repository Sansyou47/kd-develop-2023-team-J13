from flask import Blueprint, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL

mypage = Blueprint("mypage", __name__)

mysql = None

userNumber = 4  # 実装が進んだらsessionでuserNumberの値を受け取る

@mypage.route("/register_skill", methods=["POST"])
def register_skill():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    # フォームから送信された各スキルの値を取得し、データベースに格納
    for skill_index in range(1, 7):
        skill_value = request.form.get(f"skill{skill_index}")
        cur.execute(f"UPDATE skill SET skill{skill_index} = %s WHERE userNumber = %s", (skill_value, userNumber))

    conn.commit()
    cur.close()

    return redirect(url_for("mypage.add_mypage"))

@mypage.route("/mypage")
def add_mypage():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    # userNumberがデータベースに存在するか確認
    cur.execute("SELECT * FROM skill WHERE userNumber = %s", (userNumber,))
    result = cur.fetchone()
    # userNumberが存在しない場合、新しいデータベースを作成
    if result is None:
        cur.execute("""
            INSERT INTO skill (userNumber)
            VALUES (%s)
        """, (userNumber))
    # SQL実行
    cur.execute("SELECT * FROM skill")
    skills = cur.fetchall()
    # userNumberから名前を取り出す
    cur.execute("SELECT users.userName FROM users JOIN skill ON users.userNumber = skill.userNumber WHERE users.userNumber = %s", (userNumber,))
    name = cur.fetchone()

    conn.commit()
    cur.close()

    return render_template("/mypage/mypage.html", skills=skills, userNumber=userNumber, name=name)
