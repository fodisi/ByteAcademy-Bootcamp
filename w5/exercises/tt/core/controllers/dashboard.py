#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session

from core.model.account import Account


dashboard_ctrl = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard_ctrl.route('/', methods=['GET'])
def show_dashboard():
    #username = request.args.get('username')

    # pl = Account().get_account_data_by_user(username)
    # return render_template('dashboard.html', username=username, pl=pl)
    pl = Account().get_account_data_by_user(session['user'])
    return render_template('dashboard.html', pl=pl)
