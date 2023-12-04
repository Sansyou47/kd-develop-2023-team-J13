from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import test

app = Flask(__name__)

app.register_blueprint(test.app)

@app.route('/')
def index():
    return 'Test'

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

@app.route('/create_project')
def create_project():
    return render_template('/project/createproject.html')

@app.route('/create_project1')
def create_project1():
    return render_template('/project/createproject1.html')

@app.route('/create_project2')
def create_project2():
    return render_template('/project/createproject2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')