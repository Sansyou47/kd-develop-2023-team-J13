from flask import Blueprint, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL

mypage = Blueprint("mypage", __name__)

mysql = None

@mypage.route("/mypage")
def add_mypage():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    userNumber = 4
    # userNumberがデータベースに存在するか確認
    cur.execute("SELECT * FROM skill WHERE userNumber = %s", (userNumber,))
    result = cur.fetchone()
    # userNumberが存在しない場合、新しいエントリを作成
    if result is None:
        cur.execute("""
            INSERT INTO skill (userNumber)
            VALUES (%s)
        """, (userNumber))
    # SQL実行
    cur.execute("SELECT * FROM skill")
    skills = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template("/mypage/mypage.html", skills=skills, userNumber=userNumber)
