#!/usr/bin/env python3

from flask import Blueprint, render_template, request


lookup_ctrl = Blueprint('lookup', __name__, url_prefix='/lookup')

html_filename = 'lookup.html'


@lookup_ctrl.route('/', methods=['GET', 'POST'])
def show_lookup():
    pass
