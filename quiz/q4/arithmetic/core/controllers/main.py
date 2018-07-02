#!/usr/bin/env python3

from flask import Blueprint, render_template, request, jsonify

from core.model.arithmetic import Arithmetic


main_ctrl = Blueprint('main', __name__, url_prefix='/')

html_filename = 'index.html'


@main_ctrl.route('/<operation>', methods=['GET'])
def calculate(operation):
    obj = Arithmetic(operation,
                     request.args.get('num1'),
                     request.args.get('num2'))
    return jsonify(obj.to_dictionary())
