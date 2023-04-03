from flask import render_template, redirect, app, Flask
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db
from main import Developer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)


# get dev's bugs
"""
from myapp import app, db
from myapp.models import Developer

@app.route('/developers/<int:id>')
def get_developer(id):
    dev = Developer.query.get(id)
    bugs = dev.assigned_bugs
    # do something with bugs
    ...
"""

""""
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    assigned_bugs = db.relationship('Bug', backref='developer', lazy=True)

    def __repr__(self):
        return f"Developer('{self.id}', '{self.name}')"
"""


@app.route('/developer')
def developer_interface():
    if current_user.role == 'developer':
        developer = Developer.query.filter_by(name=current_user.username).first()
        bugs = developer.assigned_bugs
        return render_template('developer.html', bugs=bugs)
    return redirect('/')
