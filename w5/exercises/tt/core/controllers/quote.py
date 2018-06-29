#!/usr/bin/env python3

from flask import Blueprint, render_template, request


quote_ctrl = Blueprint('quote', __name__, url_prefix='/quote')

html_filename = 'quote.html'


@quote_ctrl.route('/', methods=['GET', 'POST'])
def show_quote():
    pass
