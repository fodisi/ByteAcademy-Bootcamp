#!usr/bin/env python3

from flask import Flask

from core.controllers.product import controller as product

omnibus = Flask(__name__)

omnibus.register_blueprint(product)
