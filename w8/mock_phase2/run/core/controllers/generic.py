#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('generic', __name__)


@controller.route('/<product_name>')
def home(product_name):
    # obj = model.get_product(product_name)

    return render_template('index.html', json_obj=obj.to_json)
