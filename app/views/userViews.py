# coding=utf-8
from run import app
from flask import render_template
from ..models.user import User

"""" Web Views """

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page/<int:page>')
def home_test(page=1):
    try:
        users = User.query.paginate(page, per_page=25)
    except OperationalError:
        flash("No users in the database.")
        users = None
    return render_template('index_page.html', users = users)
