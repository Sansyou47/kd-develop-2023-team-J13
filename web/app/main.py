from flask import Flask, render_template, request, redirect ,session
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
    return 'test'

@app.route('/create_stories', methods=['GET', 'POST'])
def storeis():
    project = session['poject']
    if request.method == 'POST':
        # POSTメソッドでの処理
        stories = request.form.get('stories')
        conn = mysql.get_db()
        cur = conn.cursor()
        try:
            #projectの追加が必要
            cur.execute("INSERT INTO story(name,project) VALUES(%s,%s)", (stories,project))
            conn.commit()
        except mysql.Error as e:
            print(f"MySQL Error: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    # 共通の処理（GETメソッドでの処理）
    conn = mysql.get_db()
    cur = conn.cursor()
    cur.execute("SELECT name FROM story WHERE project = %s",project)
    story_data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('stories/create_stories.html', story_data=story_data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')