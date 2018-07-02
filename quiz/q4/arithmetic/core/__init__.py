
#!/usr/bin/env python3

import os

from flask import Flask

from core.controllers.main import main_ctrl as main


omnibus = Flask(__name__)

# TODO create dinamic secret_key
# omnibus.secret_key = 'You Will Never Guess'


omnibus.register_blueprint(main)
