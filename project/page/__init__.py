"""
The `recipes` blueprint handles displaying recipes.
"""
from flask import Blueprint

page_blueprint = Blueprint('page', __name__, template_folder='templates')

from . import routes
