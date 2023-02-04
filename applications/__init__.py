from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///base.db'
app.config['SECRET_KEY']=os.environ.get('APP_SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from applications import routers
