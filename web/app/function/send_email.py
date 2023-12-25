from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL
from flask_login import login_required
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import os

send_email = Blueprint("send_email", __name__)

mysql = None

sendAddress = os.getenv("SEND_MAIL_ADDRESS")
password = os.getenv("SEND_MAIL_PASSWORD")

def create_email(to, subject, body):
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

@send_email.route('/project/addusers')
@login_required
def addusers():
    return render_template('/project/addusers.html')

@send_email.route('/action/project/addusers', methods=['POST'])
@login_required
def acaddusers():
    conn = mysql.get_db()
    cur = conn.cursor()
    email = request.form.get('email')
    project = str(session.get('project'))
    projectNumber = str(session.get("project_number"))
        
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
        cur.execute('INSERT INTO project_users(projectName, userId, projectNumber) VALUES(%s, %s, %s)', (project, email, projectNumber))
        conn.commit()
        subject = project + 'プロジェクトへの招待が来ています'
        body = 'あなたへの招待が来ています。' + '\n' + '以下のリンクからプロジェクトに参加してください。' + '\n' + 'http://localhost:9047/'
        create_email(email, subject, body)
        
        return redirect('/select_project')
    else:
        error_message = 'ユーザーが存在しません。'
        return render_template('/project/addusers.html', error_message=error_message)

