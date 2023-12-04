from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import test
import os

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')

mysql=MySQL(app)

app.register_blueprint(test.app)

@app.route('/')
def index():
    return 'Test'

@app.route('/project')
def project():
    return render_template('select_project.html')

@app.route('/create_storeis')
def storeis():
    return render_template('/templates/stories/create_stories.html')

@app.route('/action/create_stories',methods=['POST'])
def add_stories():
    stories = request.form.get('stories')
    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    cur.execute("INSERT INTO employee(project_int,stories_name,stories) VALUES(%s,%s,%s)",(hoge,stories,hoge))
    conn.commit()
    cur.close()
    return render_template('/templates/stories/create_stories.html')

@app.route('/select_project')
def select_project():
    # MySQLへ接続
    cur = mysql.get_db().cursor()
    # SQL実行
    cur.execute("SELECT * FROM project")
    data = cur.fetchall()
    return render_template('/select_project.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')