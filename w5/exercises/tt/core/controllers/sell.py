#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session

from core.model.order import Order
from core.model.user import User


sell_ctrl = Blueprint('sell', __name__, url_prefix='/sell')

html_filename = 'sell.html'


def sell(symbol, volume, username):
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


@sell_ctrl.route('/', methods=['GET', 'POST'])
def show_sell():
    # username = request.args.get('username')
    if request.method == 'GET':
        return render_template(html_filename, status='', error_detail='')
    else:
        return sell(request.form['symbol'], request.form['volume'], session['user'])
