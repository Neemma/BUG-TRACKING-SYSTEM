from flask import app, Flask
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)

"""
class ProjectManagers(db.Model):
    manager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(Projects.project_id), nullable=False)


def __repr__(self):
    return f"ProjectManager('{self.id}', '{self.name}')"


@main.app.route('/project_manager')
def project_manager_interface():
    if current_user.role == 'project_manager':
        project_manager = ProjectManagers.query.filter_by(name=current_user.username).first()
        projects = project_manager.projects
"""


if __name__ == '__main__':
    app.run(debug=True)