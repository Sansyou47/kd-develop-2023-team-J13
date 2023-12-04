from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import test
import os

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

app.register_blueprint(test.app)


@app.route('/')
def index():
    return render_template('/stories/create_stories.html')

@app.route('/create_storeis')
def storeis():
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行 SQLに追加：WHEREでprojectを指定
    cur.execute("SELECT name FROM story")
    story_data = cur.fechall()
    conn.commit()
    cur.close()
    return render_template('/stories/create_stories.html',story_data = story_data)

@app.route('/action/create_stories',methods=['POST'])
def add_stories():
    stories = request.form.get('stories')
    #project = request.form.get('project')
    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    #cur.execute("INSERT INTO employee(name,project) VALUES(%s,%s)",(stories,project))
    cur.execute("INSERT INTO story(name,) VALUES(%s)",(stories))
    conn.commit()
    cur.close()
    return render_template('/stories/create_stories.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')