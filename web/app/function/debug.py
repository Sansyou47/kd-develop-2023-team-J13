from flask import Flask, render_template, request, redirect, session, Blueprint
from flaskext.mysql import MySQL
from flask_login import login_required
import os

debug = Blueprint("debug", __name__)

mysql = None