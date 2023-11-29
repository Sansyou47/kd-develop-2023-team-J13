from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test'

@app.route('/suica')
def suica():
    return render_template('/project/createproject.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')