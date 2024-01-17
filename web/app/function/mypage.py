from flask import Blueprint, render_template, request, redirect, session, url_for
from flaskext.mysql import MySQL

mypage = Blueprint("mypage", __name__)

mysql = None

@mypage.route("/register_skill", methods=["POST"])
def register_skill():
    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()    
    # メアドを取得
    user_id = str(session.get("user_id"))
    
    # userNumberを取得,useridで絞ってるのは絶対に被らないから
    cur.execute("SELECT userNumber From users WHERE userId = %s", (user_id,))
    userNumber = cur.fetchone()

    # フォームから送信された各スキルの値を取得し、データベースに格納
    for skill_index in range(1, 7):
        skill_value = request.form.get(f"skill{skill_index}")
        cur.execute(f"UPDATE skill SET skill{skill_index} = %s WHERE userNumber = %s", (skill_value, userNumber))

    conn.commit()
    cur.close()

    return redirect(url_for("mypage.add_mypage"))

@mypage.route("/mypage_edit")
def add_mypage():
    # メアドを取得
    user_id = str(session.get("user_id"))
    # 名前を取得
    user_name = str(session.get("user_name"))

    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    # userNumberを取得,useridで絞ってるのは絶対に被らないから
    cur.execute("SELECT userNumber From users WHERE userId = %s", (user_id,))
    userNumber = cur.fetchone()

    # userNumberがデータベースに存在するか確認
    cur.execute("SELECT * FROM skill WHERE userNumber = %s", (userNumber,))
    result = cur.fetchone()
    # userNumberが存在しない場合、新しいデータベースを作成
    if result is None:
        cur.execute("""
            INSERT INTO skill (userNumber)
            VALUES (%s)
        """, (userNumber))
    # skillテーブルからスキルを取得,初期値の設定のため
    cur.execute("SELECT skill1, skill2, skill3, skill4, skill5, skill6 FROM skill WHERE userNumber = %s", (userNumber,))
    skills = cur.fetchall()
    conn.commit()
    cur.close()
    return render_template("/mypage/mypage.html", skills=skills, userNumber=userNumber, name=user_name)

@mypage.route("/mypage_skill")
def mypage_skill():
    # メアドを取得
    user_id = str(session.get("user_id"))
    # 名前を取得
    user_name = str(session.get("user_name"))

    # MySQLへ接続
    conn = mysql.get_db()
    cur = conn.cursor()

    
    conn.commit()
    cur.close()

    return render_template("/mypage/mypage_skill.html")
#画面更新処理が未実装