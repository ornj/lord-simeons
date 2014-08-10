from flask import Blueprint, render_template

from ..models import food_item_repository as repository



module = Blueprint('menu', __name__, url_prefix='/')


@module.route('/')
def index():
    food_items = repository.find_all()
    return render_template('menu/index.html', food_items=food_items)
