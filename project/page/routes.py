from . import page_blueprint
from flask import render_template, abort




@page_blueprint.route('/')
def recipes():
    return render_template('recipes/home.html')




