from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
  app=Flask(__name__)
  app.config['SECRET_KEY']="nothing"
  app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
  db.init_app(app)
  
  from .auth import auth
  from .views import views
  from .models import User,Note

  app.register_blueprint(views,url_prefix='/')
  app.register_blueprint(auth,url_prefix='/')
  
  return app