from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import Report

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)



def retrieve_reports_from_db():
    return Report.query.all()
