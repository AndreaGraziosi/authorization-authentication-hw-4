from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################
#This will create a login manager and initialize it with our app. We are also telling the login manager 
# where to find the login route, namely that it's inside of the auth blueprint and is called login.
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

#This tells the login manager how to load a user with a particular id. We're using 
# Flask-SQLAlchemy for this project, but technically, you could use any other database, 
# or even make up your own User object!

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt(app)

###########################
# Blueprints
###########################
from grocery_app.routes import main
app.register_blueprint(main)

from grocery_app.routes import auth
app.register_blueprint(auth)

with app.app_context():
    db.create_all()
