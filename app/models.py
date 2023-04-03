
"""
class Testers(db.Model):
    __tablename__ = "testers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def json(self):
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role
        }
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)

project_tester_association_table = db.Table('project_tester_association',
                                            db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                                            db.Column('tester_id', db.Integer, db.ForeignKey('tester.id'))
                                            )

project_developer_association_table = db.Table('project_developer_association',
                                               db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                                               db.Column('dev_id', db.Integer, db.ForeignKey('dev.id'))
                                               )
