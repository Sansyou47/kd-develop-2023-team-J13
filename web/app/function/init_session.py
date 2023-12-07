from flask import Blueprint, render_template, request, redirect, session
from flaskext.mysql import MySQL

init_session = Blueprint("init_session", __name__)

mysql = None

# セッションに値を格納
@init_session.route("/set_session")
def set_session():
    project = request.args.get("project")
    session["project"] = project
    # テストのため一時的に変更
    return redirect("/create_stories")