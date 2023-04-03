from datetime import datetime
from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from main import Projects

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy()

"""
class Developer(db.Model):
    dev_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    assigned_bugs = db.relationship('Bugs', backref='developer')
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Testers(db.Model):
    tester_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(Projects.project_id), nullable=False)


class Bugs(db.Model):
    bug_id = db.Column(db.Integer, primary_key=True)
    bug_title = db.Column(db.String(100), nullable=False)
    bug_description = db.Column(db.Text, nullable=False)
    tester_id = db.Column(db.Integer, db.ForeignKey(Testers.tester_id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    dev_id = db.Column(db.Integer, db.ForeignKey(Developer.dev_id), nullable=False)
    developer = db.relationship('Developer', backref='assigned_bugs')
    status = db.Column(db.String(20))
    priority = db.Column(db.String(20), nullable=False)

bugs_bp = Blueprint("bugs", __name__)  # WHAT THE FUCK IS THIS!!!!!!!!!11


def retrieve_bugs_from_db():
    bugs = Bugs.query.all()
    return bugs


# Call the retrieve_bugs_from_db() function to retrieve all bugs
bugs: object = retrieve_bugs_from_db()

# Loop through the list of bugs and print their details
for bug in bugs:
    print("Bug ID:", bug.id)
    print("Bug Title:", bug.title)
    print("Bug Description:", bug.description)
    print("\n")


@bugs_bp.route("/bugs", methods=["GET", "POST"])
def bugs():
    if request.method == "POST":
        # Add a new bug
        bug_details = request.form
        # Save the bug to the database
        # ...

    # Retrieve the list of bugs from the database
    bugs = retrieve_bugs_from_db()

    return render_template("bugs.html", bugs=bugs)


def retrieve_bug_from_db(bug_id):
    return Bugs.query.get(bug_id)


@bugs_bp.route("/bugs/<int:bug_id>", methods=["GET", "POST"])
def bug_detail(bug_id):
    if request.method == "POST":
        # Update the bug
        bug_details = request.form
        # Update the bug in the database
        # ...

    # Retrieve the details of a single bug from the database
    bug = retrieve_bug_from_db(bug_id)

    return render_template("bug_detail.html", bug=bug)
"""