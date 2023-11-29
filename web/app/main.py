from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import test

app = Flask(__name__)

app.register_blueprint(test.app)

@app.route('/')
def index():
    return 'Test'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')