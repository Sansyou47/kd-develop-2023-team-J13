from flask import Blueprint, render_template, request, redirect
from flaskext.mysql import MySQL

graph = Blueprint("graph", __name__)

@graph.route("/graph")
def graphs():
    return render_template("graph.html")