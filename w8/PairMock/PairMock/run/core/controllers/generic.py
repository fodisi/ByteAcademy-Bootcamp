#!/usr/bin/env python3

from flask import Blueprint, render_template
from core.model.product import Product

controller = Blueprint('generic', __name__)

@controller.route('/<product_name>')
def home(product_name):
    product = Product().get_product(product_name)
    return render_template('product.html',product = product)
