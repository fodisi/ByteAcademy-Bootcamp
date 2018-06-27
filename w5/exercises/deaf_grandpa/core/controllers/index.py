#!/usr/bin/env python3


from flask import Blueprint, render_template

controller = Blueprint('index', __name__, url_prefix='/')


@controller.route('/', methods=['GET'])
def index():
    return render_template('index.html')
