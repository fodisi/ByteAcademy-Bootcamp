#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session

from core.model.order import Order
from core.model.user import User


buy_ctrl = Blueprint('buy', __name__, url_prefix='/buy')

html_filename = 'buy.html'


def buy(symbol, volume, username):
    status = ''
    error_detail = ''
    try:
        status = Order().buy(symbol, int(volume), username)
        if status == 'NO_FUNDS':
            error_detail = User().get_current_balance(username)
    except Exception as e:
        status = 'EXCEPTION'
        error_detail = e.args[0]

    return render_template(html_filename,
                           username=username,
                           status=status,
                           error_detail=error_detail)


@buy_ctrl.route('/', methods=['GET', 'POST'])
def show_buy():
    if request.method == 'GET':
        return render_template(html_filename, status='', error_detail='')
    else:
        return buy(request.form['symbol'], request.form['volume'], session['user'])
