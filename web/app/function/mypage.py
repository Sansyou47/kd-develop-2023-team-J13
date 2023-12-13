from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

mypage = Blueprint("mypage", __name__)

mysql = None


# mypage画面
@mypage.route("/mypage")
def add_mypage():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()
    # SQL実行
    # cur.execute("SELECT * FROM task")
    # taskData = cur.fetchall()

    conn.commit()
    cur.close()

    return render_template("/mypage/mypage.html")
