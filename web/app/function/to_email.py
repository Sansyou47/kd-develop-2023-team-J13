from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import os

to_email = Blueprint("to_email", __name__)

mysql = None

sendAddress = os.getenv("SEND_MAIL_ADDRESS")
password = os.getenv("SEND_MAIL_PASSWORD")

def send_email(to, subject, body):
    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sendAddress
    msg['To'] = to
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()
    
    return

@to_email.route('/project/addusers')
@login_required
def addusers():
    return render_template('/project/addusers.html')

@to_email.route('/action/project/addusers', methods=['POST'])
@login_required
def acaddusers():
    conn = mysql.get_db()
    cur = conn.cursor()
    email = request.form.get('email')
    project = str(session.get('project'))
        
    # 入力されたメールアドレスが登録されているか確認
    cur.execute("SELECT * FROM users WHERE userId = %s", (email))
    user = cur.fetchone()
    # メールアドレスが登録されていた場合
    if user:
        cur.execute('SELECT userId FROM project_users WHERE projectName = %s AND userId = %s', (project, email))
        onuser = cur.fetchone()
        if onuser:
            error_message = 'そのユーザーは既にプロジェクトに参加しています。'
            return render_template('/project/addusers.html', error_message=error_message)
        cur.execute('INSERT INTO project_users(projectName, userId) VALUES(%s, %s)', (project, email))
        conn.commit()
        subject = project + 'プロジェクトへの招待が来ています'
        body = 'あなたへの招待が来ています。' + '\n' + '以下のリンクからプロジェクトに参加してください。' + '\n' + 'http://localhost:9047/'
        send_email(email, subject, body)
        
        return redirect('/select_project')
    else:
        error_message = 'ユーザーが存在しません。'
        return render_template('/project/addusers.html', error_message=error_message)
