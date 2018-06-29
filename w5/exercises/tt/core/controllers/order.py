#!/usr/bin/env python3

from flask import Blueprint, render_template, request


order_ctrl = Blueprint('order', __name__, url_prefix='/order')

html_filename = 'order.html'


@order_ctrl.route('/', methods=['GET', 'POST'])
def show_order():
    pass
