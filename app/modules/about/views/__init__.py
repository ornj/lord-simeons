from flask import Blueprint, render_template


module = Blueprint('about', __name__, url_prefix='/about')


@module.route('/')
def index():
    return render_template('about/index.html')
