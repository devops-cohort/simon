from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@35.242.133.237/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'm8c4m5c899284m'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)

from application.models import Users, Posts

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Users.query.filter_by(id=id).first()

login_manager.user_loader(load_user)

from application import routes


