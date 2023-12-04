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
    cur.execute("INSERT INTO employee(stories_name,project) VALUES(%s,%s)",(stories,hoge))
    conn.commit()
    cur.close()
    return render_template('/templates/stories/create_stories.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')