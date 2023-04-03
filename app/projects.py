from datetime import datetime

from flask import render_template, redirect, app, Flask, request, url_for

from flask_sqlalchemy import SQLAlchemy
from models import project_tester_association_table, project_developer_association_table


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)

"""
class Projects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey(ProjectManagers.manager_id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    # testers assigned here
    testers = db.relationship('Tester', secondary=project_tester_association_table,
                              backref=db.backref('projects', lazy=True))
    # developers assigned here
    developers = db.relationship('Developer', secondary=project_developer_association_table,
                                 backref=db.backref('projects', lazy=True))


with app.app_context():
    db.create_all()
"""
if __name__ == '__main__':
    app.run(debug=True)