import json

from flask import Blueprint, render_template

pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint(
    'pet',
    __name__,
    url_prefix = '/pets'
)

@bp.route('/')
def index():
    return render_template('pets/index.html', pets = pets)

@bp.route('/<int:id>')
def show(id):
    return render_template('pets/show.html', pets = pets)