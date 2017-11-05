from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db, photos
from flask_login import login_required,current_user
from ..models import User


@main.route('/')
def index():

    title="Helo world"
    return render_template('index.html',title=title)

        