#!/usr/bin/env python3

from flask import Blueprint, render_template, request

from core.model.user import User

controller = Blueprint('login', __name__)


def try_login(username, password):
    user = User().login(username, password)
    return user != None, user


@controller.route('/', methods=['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['email']
        password = request.form['password']
        result, user = try_login(username, password)
        if result:
            return render_template('dashboard.html')
        else:
            return render_template('login.html')
