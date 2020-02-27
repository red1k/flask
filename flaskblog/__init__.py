from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b4d17b47db61ccb90f2cedfed7859bb4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# database
db = SQLAlchemy(app)

# password encryption
bcrypt = Bcrypt(app)

# login page related
login_manager = LoginManager(app)

login_manager.login_view = 'login'              # 'login' -> function name of route
login_manager.login_message_category = 'info'   # 'info'  -> bootstrap class name

from flaskblog import routes
