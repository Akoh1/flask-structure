from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
# from app.models import User, Newuser
from . import home as home_blueprint
import os
from app import database


# @home_blueprint.route('/all/users', methods=['GET'])
# def all_users():
#     """
#     List all Users
#     """
#     all_users = User.query.all()
#     return render_template('home/home.html', users=all_users, title="Users")


@home_blueprint.route("/")
def home():
 
    return render_template('home.html')
