# bs3d/website/views.py
# Black Swan 3D Printing
#
# https://blackswan3d.com/

from flask import render_template, Blueprint, redirect

bp = Blueprint('website', __name__,
               template_folder='templates',
               static_folder='static')

@bp.route("/")
def index():
    return redirect('/about/')

@bp.route('/showcase/')
def showcase():
    return render_template('showcase.html')

@bp.route("/about/")
def about():
    return render_template("about.html")

@bp.route("/our-team/")
def team():
    return render_template("our_team.html")
