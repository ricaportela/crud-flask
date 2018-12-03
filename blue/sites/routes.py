from flask import Blueprint

mod = Blueprint('sites', __name__)

@mod.route('/homepage')
def homepage():
    return '<h1> Voce esta na home page</h1>'