#!/usr/bin/env python3

from flask import Blueprint, render_template, request

from core.model.order import Order

lookup_ctrl = Blueprint('lookup', __name__, url_prefix='/lookup')

html_filename = 'lookup.html'


def __lookup(company_name):
    company = None
    error = None
    try:
        symbol = Order().get_ticker_symbol(company_name)
        company = {'name': company_name, 'symbol': symbol}
    except Exception as e:
        error = e.args[0]

    return render_template(html_filename, company=company, error=error)


@lookup_ctrl.route('/', methods=['GET', 'POST'])
def show_lookup():
    if request.method == 'GET':
        return render_template(html_filename)
    else:
        return __lookup(request.form['company'])
