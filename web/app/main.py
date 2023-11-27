from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test'