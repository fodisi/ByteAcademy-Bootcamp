#!/usr/bin/env python3


from flask import Blueprint, render_template, request


#controller = Blueprint('general', __name__, url_prefix='/')
controller = Blueprint('general', __name__)


@controller.route('/', methods=['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # assume is a post request
        username = request.form['email']
        password = request.form['password']
        #print(username, password)
        if username != 'me@mail.com' or password != 'swordfish':
            return render_template('login.html')
        else:
            return render_template('dashboard.html')


@controller.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ticker_symbols = ['aapl', 'amzn', 'fb', 'googl', 'msft']
        if request.form['search'] in ticker_symbols:
            return render_template('dashboard.html')
        else:
            return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')
