import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

SECRET_KEY = "some secret"

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from players.api.views import player
app.register_blueprint(player)


with app.app_context():
    db.create_all()

    
    

