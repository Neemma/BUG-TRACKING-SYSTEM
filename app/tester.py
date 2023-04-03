from datetime import datetime
from flask import render_template, redirect, app, Flask, request, url_for
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db
from main import Bugs, Projects, Testers


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)
# app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/tester')
def tester_dashboard():
    tester = Testers.query.first()
    # Get a list of the tester's current and previous projects
    current_projects = tester.projects.filter_by(completed=False).all()
    previous_projects = tester.projects.filter_by(completed=True).all()

    # Get a list of the tester's reported bugs
    reported_bugs = tester.bugs.all()

    return render_template('tester.html',
                           tester=tester,
                           current_projects=current_projects,
                           previous_projects=previous_projects,
                           reported_bugs=reported_bugs)


@app.route('/tester/report_bug', methods=['GET', 'POST'])
def report_bug():
    if request.method == 'POST':
        # Get the bug description and project ID from the form
        description = request.form['description']
        project_id = request.form['project_id']

        # Create a new Bug object with the description, the current date and time, and the project ID
        bug = Bugs(description=description, created_at=datetime.now(), project_id=project_id)

        # Add the new bug to the database and commit the transaction
        db.session.add(bug)
        db.session.commit()

        # Redirect the user to a success page
        return render_template('report_bug_success.html')

    else:
        # Get a list of projects for the user to choose from
        projects = Projects.query.filter_by(tester_id=current_user.id).all()

        # Render the report bug form with the list of projects
        return render_template('report_bug.html', projects=projects)








"""
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form['username']
    password = request.form['password']

    if name in Testers and Testers[name] == password:
        return redirect(url_for('tester_dashboard'))
    else:
        return 'Invalid username or password'


@app.route('/tester')
def tester_dashboard():
    tester_projects = [project for project in Projects if project['project_id'] in [1, 2]]
    tester_bugs = [bug for bug in Bugs if bug['project_id'] in [1, 2]]
    return render_template('tester.html', projects=tester_projects, bugs=tester_bugs)


if __name__ == '__main__':
    app.run(debug=True)
"""