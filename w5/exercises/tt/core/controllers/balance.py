#!/usr/bin/env python3

from flask import Blueprint, render_template, request


balance_ctrl = Blueprint('balance', __name__, url_prefix='/balance')

html_filename = 'balance.html'


@balance_ctrl.route('/', methods=['GET', 'POST'])
def show_balance():
    pass
