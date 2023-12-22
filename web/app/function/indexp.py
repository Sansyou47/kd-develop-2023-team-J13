from flask import Blueprint, render_template, session

indexp=Blueprint('indexp',__name__)

@indexp.route('/')
def index():
    # セッションから値を取得
    data=str(session.get('project'))
    return render_template('index.html',data=data)