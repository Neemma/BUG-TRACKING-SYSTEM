import re
import secrets
import uuid
from datetime import datetime
from email import encoders
from datetime import datetime
import textwrap

from email.mime.base import MIMEBase

import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import smtplib
from reportlab.pdfgen import canvas
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import mysql.connector
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from mailbox import Message

import bcrypt as bcrypt
import mail as mail
from flask import Flask, render_template, request, redirect, url_for, session, flash, config, abort
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import smtplib
import random
import string
import mysql.connector
from mysql.connector import cursor
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from models import project_tester_association_table, project_developer_association_table, db

# Connect to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/joinus.html')
def joinus():
    return render_template('joinus.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/usersupport.html')
def usersupport():
    return render_template('usersupport.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


# CONTACT US FORM
@app.route('/contactus', methods=['POST'])
def contactus():
    # Get form data
    first_name = request.form['fname']
    last_name = request.form['lname']
    user_email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Send email to the buibui
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    techteam_email = 'techteam.buibuibugtracking@gmail.com'
    password = 'zfgvqxnaglxlqajc'
    message = f'Subject: New Message {subject}\n\n' \
              f'Message: {message}\n' \
              f'User: {first_name} {last_name}\n' \
              f'User Email: {user_email}\n'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, techteam_email, message)
    # Send email to the user
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    receiver_email = user_email
    password = 'zfgvqxnaglxlqajc'
    message = f'Subject: Message Received\n\n' \
              f'Dear {first_name},\n\n' \
              f'We have received your message regarding {subject}.\n' \
              f'Thank you for contacting us. ' \
              f'You will receive a response from our team based on the nature of your message\n\n' \
              f'If you are having any issues with our systems, kindly visit our User Support page\n\n' \
              f'Best regards,\n' \
              f'The BuiBui Team'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, message)
    return 'Form submitted successfully!'


@app.route('/REPORTBUgG.html')
def reportbug():
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!',
                                  host='localhost', database='bugtrackingsystem120')
    cursor = cnx.cursor()

    tester_id = session.get('tester_id')

    get_tester_projects = "SELECT project_id, project_title FROM projects WHERE project_id IN (SELECT project_id FROM project_testers WHERE tester_id = %s)"
    cursor.execute(get_tester_projects, (tester_id,))
    projects = cursor.fetchall()

    get_tester_projects = "SELECT project_id, project_title FROM projects WHERE project_id IN (SELECT project_id FROM project_testers WHERE tester_id = %s)"
    cursor.execute(get_tester_projects, (tester_id,))
    projectss = cursor.fetchall()
    # Close database connection
    cursor.close()
    cnx.close()

    # Render the template with the project options
    return render_template('REPORTBUgG.html', projects=projects, projectss=projectss)


@app.route('/testerlogin.html')
def testerlogin():
    return render_template('testerlogin.html')


"""
@app.route('/changepassword')
def changepassword():
    return render_template('testerchangepassword.html')


@app.route('/update_password', methods=['POST'])
def update_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # Verify that the current password is correct
    if check_password_hash(current_password, testerlogin().password):
        # Verify that the new password and confirm password fields match
        if new_password == confirm_password:
            # Check if the new password meets the complexity requirements
            if len(new_password) < 8:
                flash('Password should be at least 8 characters long.')
            elif not re.search("[a-z]", new_password):
                flash('Password should contain at least one lowercase letter.')
            elif not re.search("[A-Z]", new_password):
                flash('Password should contain at least one uppercase letter.')
            elif not re.search("[0-9]", new_password):
                flash('Password should contain at least one digit.')
            elif not re.search("[@#$%^&+=]", new_password):
                flash('Password should contain at least one special character (@#$%^&+=).')
            else:
                # Hash the new password and update the user's record in the database
                new_password_hash = generate_password_hash(new_password)
                testerlogin.password = new_password_hash
                db.session.commit()
                flash('Password updated successfully.')
        else:
            flash('New password and confirm password do not match.')
    else:
        flash('Incorrect current password.')

    return redirect(url_for('testerprofile'))

"""


@app.route('/developerlogin.html')
def developerlogin():
    return render_template('developerlogin.html')


@app.route('/managerlogin.html')
def managerlogin():
    return render_template('managerlogin.html')


@app.route('/addusers.html')
def addusers():
    return render_template('addusers.html')


@app.route('/adminlogin.html')
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/testerform.html')
def testerform():
    return render_template('testerform.html')


@app.route('/developerform.html')
def developerform():
    return render_template('developerform.html')


@app.route('/managerform.html')
def managerform():
    return render_template('managerform.html')


@app.route('/createproject.html')
def createproject():
    return render_template('createproject.html')


# Define database models
class ProjectManagers(db.Model):
    manager_id = db.Column(db.Integer, primary_key=True)
    mfname = db.Column(db.String(100), nullable=False)
    mlname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(50))


# project_id = db.Column(db.Integer, db.ForeignKey('project_id'), nullable=False)


class Projects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    # manager_id = db.Column(db.Integer, db.ForeignKey('ProjectManagers.manager_id'), nullable=False)
    # ProjectManagers = db.relationship('ProjectManagers', backref = 'Projects')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    # testers assigned here
    # testers = db.relationship('Tester', secondary=project_tester_association_table,
    # backref=db.backref('projects', lazy=True))
    # developers assigned here
    developers = db.relationship('Developer', secondary=project_developer_association_table,
                                 backref=db.backref('projects', lazy=True))


class Developer(db.Model):
    dev_id = db.Column(db.Integer, primary_key=True)
    dfname = db.Column(db.String(100), nullable=False)
    dlname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    assigned_bugs = db.relationship('Bugs', backref='developer')
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(50))


class Testers(db.Model):
    tester_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # project_id = db.Column(db.Integer, db.ForeignKey(Projects.project_id), nullable=False)
    # bugs_reported = db.Column(db.Integer, default=0)
    # ranking = db.Column(db.Integer, default=0)
    phone_number = db.Column(db.String(50))


class Bugs(db.Model):
    bug_id = db.Column(db.Integer, primary_key=True)
    bug_title = db.Column(db.String(100), nullable=False)
    bug_description = db.Column(db.Text, nullable=False)
    # tester_id = db.Column(db.Integer, db.ForeignKey(Testers.tester_id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # dev_id = db.Column(db.Integer, db.ForeignKey(Developer.dev_id), nullable=False)
    developer = db.relationship('Developer', backref='assigned_bugs')
    status = db.Column(db.String(20))
    priority = db.Column(db.String(20), nullable=False)


# project_id = db.Column(db.Integer, db.ForeignKey(Projects.project_id), nullable=False)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


# Function to get the project manager of a project
def get_project_pm(project_id):
    # Query the database to get the project manager of the given project id
    query = "SELECT manager_id FROM projects WHERE id = %s"
    cursor.execute(query, (project_id,))
    result = cursor.fetchone()
    if result:
        pm_id = result[0]
        # Query the database to get the project manager's email address
        query = "SELECT email FROM users WHERE id = %s"
        cursor.execute(query, (pm_id,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the email address of the project manager
    return None


# Function to send a notification message to a user
def send_notification(manager_id, subject, message):
    # Query the database to get the email address of the user
    query = "SELECT email FROM project_managers WHERE id = %s"
    cursor.execute(query, (manager_id,))
    result = cursor.fetchone()
    if result:
        email = result[0]
        # Code to send the email notification using a library like smtplib
        # This is just an example, you should use a proper library and configure your email server settings
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('buibuibugtracking1.2.0@gmail.com', 'zfgvqxnaglxlqajc')
        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail("sender_email_address", email, msg)
        server.quit()


# REPORT BUG
@app.route('/report_bug', methods=['POST'])
def report_bug():
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!',
                                  host='localhost', database='bugtrackingsystem120')
    cursor = cnx.cursor()

    tester_id = session.get('tester_id')

    get_tester_projects = "SELECT p.project_id, p.project_title FROM project_testers pt JOIN projects p ON pt.project_id = p.project_id WHERE pt.tester_id = %s"
    cursor.execute(get_tester_projects, (tester_id,))
    projects = cursor.fetchall()

    if request.method == 'POST':
        # Get form data
        bug_title = request.form['short_desc']
        bug_description = request.form['bug_steps']
        actual_results = request.form['actual']
        expected_results = request.form['expected']
        bug_type = request.form['bug_type']
        project_id = request.form['project_id']
        environment = request.form['environment']
        #   bug_image = request.form['file']
        bug_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!',
                                      host='localhost', database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get project id for the given project title
        cursor.execute("SELECT project_title FROM projects WHERE project_id = %s", (project_id,))
        project_title = cursor.fetchone()[0]
        # Insert bug report into database
        add_bug_report = ("INSERT INTO bugs "
                          "(bug_id, bug_title, bug_description, actual_results, expected_results, bug_type, tester_id, project_title, environment, project_id) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)")
        bug_report_data = (
            bug_id, bug_title, bug_description, actual_results, expected_results, bug_type, tester_id,
            project_title, environment, project_id)
        cursor.execute(add_bug_report, bug_report_data)

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return 'Bug reported successfully'

    # Render the bug reporting form with the project dropdown list
    return render_template('REPORTBUgG.html', projects=projects)


"""
    # Send email to project manager
    msg = MIMEMultipart()
    msg['From'] = 'buibuibugtracking1.2.0@gmail.com'
    msg['To'] = 'mutubaneema@gmail.com'
    msg['Subject'] = 'New Bug Report'
    body = f'A new bug report has been submitted for project {project}.'
    msg.attach(MIMEText(body, 'plain'))

    #  sender_password = 'zfgvqxnaglxlqajc'

    # Attach file if uploaded
    if 'data' in request.files:
        file = request.files['data']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
                attach = MIMEApplication(f.read(), Name=filename)
            attach['Content-Disposition'] = f'attachment; filename={filename}'
            msg.attach(attach)

    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('buibuibugtracking1.2.0@gmail.com', 'zfgvqxnaglxlqajc')
    text = msg.as_string()
    server.sendmail('buibuibugtracking1.2.0@gmail.com', 'mutubaneema@gmail.com', text)
    server.quit()

    # Redirect user to success page
    return redirect(url_for('success'))
"""


# CREATE NEW PROJECT
@app.route('/newproject', methods=['POST'])
def newproject():
    # GET FORM DATA
    project_title = request.form['project_title']
    project_description = request.form['project_description']
    deadline = request.form['deadline']
    manager_id = request.form['manager_id']
    project_type = request.form['project_type']
    manager = request.form['manager']
    manager_email = request.form['manager_email']
    project_stakeholder_email = request.form['project_stakeholder_email']
    project_stakeholder_phone = request.form['project_stakeholder_phone']

    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!',
                                  host='localhost', database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Insert new project into database
    add_project = ("INSERT INTO projects "
                   "(project_title, project_description, deadline, manager_id, manager_email, project_type,project_stakeholder_email,project_stakeholder_phone) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    project_data = (
        project_title, project_description, deadline, manager_id, manager_email, project_type,
        project_stakeholder_email,
        project_stakeholder_phone)
    cursor.execute(add_project, project_data)

    # Retrieve the project_id value for the newly inserted project
    project_id = cursor.lastrowid

    # Insert the new project manager into the project_projectmanagers table
    add_project_manager = ("INSERT INTO project_projectmanagers "
                           "(project_id, manager_id) "
                           "VALUES (%s, %s)")
    project_manager_data = (project_id, manager_id)
    cursor.execute(add_project_manager, project_manager_data)

    # Commit changes to database
    cnx.commit()

    # Close database connection
    cursor.close()
    cnx.close()

    # Send email with login details
    subject = f'New Project: {project_title}'
    body = f'Dear {manager},\n\nA new project "{project_title}" (id:{project_id}) has been assigned to you.\n\nPlease login to the bug tracking system to view and manage the project.\n\nBest regards,\n\nBuiBui Bug Tracking :)'
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'

    recipient_email = manager_email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{body}')

    return 'Project created and email sent to project manager'


# ADD TESTER
@app.route('/add_tester', methods=['POST'])
def add_tester():
    # Get form data
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phone_number = request.form['phone']
    address = request.form['address']

    # Generate unique username and password
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    tester_id = ''.join(random.choices(string.digits, k=4))

    # Insert data into database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='bugtrackingsystem120')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Testers (tester_id, fname, lname, email, phone_number, address, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (tester_id, fname, lname, email, phone_number, address, username, password))
    conn.commit()

    # Send email with login details
    subject = 'BUIBUI TESTER DETAILS'
    body = f"Hello {fname} {lname},\n\nYour tester account has been created. Please use the following credentials to login:\nUsername: {username}\nPassword: {password}\nTester ID: {tester_id}"
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'

    recipient_email = email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{body}')

    return 'Tester added successfully!'


# ADD DEVELOPER
@app.route('/add_developer', methods=['POST'])
def add_developer():
    # Get form data
    dfname = request.form['fname']
    dlname = request.form['lname']
    email = request.form['email']
    phone_number = request.form['phone']
    address = request.form['address']

    # Generate unique username and password
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    dev_id = ''.join(random.choices(string.digits, k=4))

    # Insert data into database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='bugtrackingsystem120')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Developer (dev_id, dfname, dlname, email, phone_number, address, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (dev_id, dfname, dlname, email, phone_number, address, username, password))
    conn.commit()

    # Send email with login details
    subject = 'BUIBUI DEVELOPER DETAILS'
    body = f"Hello {dfname} {dlname},\n\nYour Developer account has been created. Please use the following credentials to login:\nUsername: {username}\nPassword: {password}\nDeveloper ID: {dev_id}"
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'

    recipient_email = email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{body}')

    return 'Developer added successfully!'


# ADD PROJECT MANAGER
@app.route('/add_manager', methods=['POST'])
def add_manager():
    # Get form data
    mfname = request.form['fname']
    mlname = request.form['lname']
    email = request.form['email']
    phone_number = request.form['phone']
    address = request.form['address']

    # Generate unique username and password
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    manager_id = ''.join(random.choices(string.digits, k=4))

    # Insert data into database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='bugtrackingsystem120')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Project_Managers (manager_id, mfname, mlname, email, phone_number, address, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (manager_id, mfname, mlname, email, phone_number, address, username, password))
    conn.commit()

    # Send email with login details
    subject = 'BUIBUI MANAGER DETAILS'
    body = f"Hello {mfname} {mlname},\n\nYour Project Manager account has been created. Please use the following credentials to login:\nUsername: {username}\nPassword: {password}\nProject Manager ID: {manager_id}"
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'

    recipient_email = email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{body}')

    return 'Project Manager added successfully!'


# TESTER LOGIN
@app.route('/login_tester', methods=['GET', 'POST'])
def login_tester():
    if request.method == 'GET':
        return render_template('testerlogin.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='BUGTRACKINGSYSTEM120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Testers WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['tester_id'] = user[0]
            return redirect('/testerdashboard')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('testerlogin.html', error=error)


@app.route('/testerlogout')
def testerlogout():
    # clear the session data
    session.clear()
    # redirect to the login page
    return redirect(url_for('login_tester'))


@app.route('/testerdashboard')
def testerdashboard():
    # Check if user is logged in
    if 'tester_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Testers WHERE tester_id=%s", (session['tester_id'],))
    user = cursor.fetchone()

    # Get user's name from the database
    cursor.execute("SELECT fname FROM Testers WHERE tester_id=%s", (session['tester_id'],))
    fname = cursor.fetchone()[0]

    # Fetch bugs reported by this tester
    cursor.execute("SELECT * FROM bugs WHERE tester_id=%s AND status IN ('OPEN', 'IN-PROGRESS', 'RESOLVED')",
                   (session['tester_id'],))
    bugs = cursor.fetchall()

    # Fetch archived bugs(bugs whose status = CLOSED)
    cursor.execute("SELECT * FROM bugs WHERE tester_id=%s AND status='CLOSED'", (session['tester_id'],))
    archbugs = cursor.fetchall()

    # Get the current date and time
    current_datetime = datetime.now()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_testers pt ON p.project_id = pt.project_id " \
            "WHERE pt.tester_id = %s AND p.deadline > %s"

    # Execute the query with the parameters
    cursor.execute(query, (session['tester_id'], current_datetime,))
    projects = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_testers pt ON p.project_id = pt.project_id " \
            "WHERE pt.tester_id = %s AND p.deadline < %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['tester_id'], current_datetime,))
    projectss = cursor.fetchall()

    tester_id = session.get('tester_id')
    # Notification count
    get_notification_count_query = "SELECT COUNT(*) FROM tester_notifications WHERE tester_id = %s AND is_read = 0"
    cursor.execute(get_notification_count_query, (str(tester_id),))
    notification_count = cursor.fetchone()[0]

    # Retrieving notifications for a user
    get_notifications_query = "SELECT * FROM tester_notifications WHERE tester_id = %s AND is_read = 0 ORDER BY created_at DESC"
    cursor.execute(get_notifications_query, (tester_id,))
    notifications = cursor.fetchall()
    # Commit changes to database
    conn.commit()
    # Close database connection
    cursor.close()
    conn.close()

    return render_template('testerdashboard.html', user=user, fname=fname, bugs=bugs, projects=projects,
                           projectss=projectss, archbugs=archbugs, notifications=notifications, notification_count=notification_count)


@app.route('/mark_notification_read/<int:notification_id>')
def mark_notification_read(notification_id):
    # Connect to database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
    cursor = conn.cursor()

    # Update the notification record in the database
    mark_notification_read_query = "UPDATE tester_notifications SET is_read = 1 WHERE notification_id = %s"
    cursor.execute(mark_notification_read_query, (notification_id,))
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()

    return redirect(url_for('testerdashboard'))


# MANAGER MARK NOTIFICATION AS READ
@app.route('/managermark_notification_read/<int:notification_id>')
def managermark_notification_read(notification_id):
    # Connect to database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
    cursor = conn.cursor()

    # Update the notification record in the database
    mark_notification_read_query = "UPDATE manager_notifications SET is_read = 1 WHERE notification_id = %s"
    cursor.execute(mark_notification_read_query, (notification_id,))
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()

    return redirect(url_for('managerdashboard'))


# DEVELOPER LOGIN
@app.route('/login_developer', methods=['GET', 'POST'])
def login_developer():
    if request.method == 'GET':
        return render_template('developerlogin.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='BUGTRACKINGSYSTEM120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Developer WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['dev_id'] = user[0]
            return redirect('/developerdashboard')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('developerlogin.html', error=error)


@app.route('/developerlogout')
def developerlogout():
    # clear the session data
    session.clear()
    # redirect to the login page
    return redirect(url_for('login_developer'))


# DEVELOPER DASHBOARD
@app.route('/developerdashboard')
def developerdashboard():
    # Check if user is logged in
    if 'dev_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM developer WHERE dev_id=%s", (session['dev_id'],))
    user = cursor.fetchone()

    # Get user's name from the database
    cursor.execute("SELECT dfname FROM developer WHERE dev_id=%s", (session['dev_id'],))
    dfname = cursor.fetchone()[0]

    # Get the current date and time
    current_datetime = datetime.now()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_developers pt ON p.project_id = pt.project_id " \
            "WHERE pt.dev_id = %s AND p.deadline > %s"

    # Execute the query with the parameters
    cursor.execute(query, (session['dev_id'], current_datetime,))
    projects = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_developers pt ON p.project_id = pt.project_id " \
            "WHERE pt.dev_id = %s AND p.deadline < %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['dev_id'], current_datetime,))
    projectss = cursor.fetchall()

    dev_id = session.get('dev_id')

    get_bugs3 = "SELECT * FROM bugs b " \
                "JOIN developer_bugs db ON b.bug_id = db.bug_id " \
                "WHERE dev_id = %s AND b.status IN ('OPEN', 'IN-PROGRESS', 'RESOLVED')"
    cursor.execute(get_bugs3, (dev_id,))
    bugs3 = cursor.fetchall()

    # bugs whose status= closed
    archbugs = "SELECT * FROM bugs b " \
                "JOIN developer_bugs db ON b.bug_id = db.bug_id " \
                "WHERE db.dev_id = %s AND b.status = 'CLOSED'"
    cursor.execute(archbugs, (dev_id,))
    archbugs = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_developers pt ON p.project_id = pt.project_id " \
            "WHERE pt.dev_id = %s AND p.deadline > %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['dev_id'], current_datetime,))
    projectsss = cursor.fetchall()

    dev_id = session.get('dev_id')
    # Notification count
    get_notification_count_query = "SELECT COUNT(*) FROM developer_notifications WHERE dev_id = %s AND is_read = 0"
    cursor.execute(get_notification_count_query, (str(dev_id),))
    notification_count = cursor.fetchone()[0]

    # Retrieving notifications for a user
    get_notifications_query = "SELECT * FROM developer_notifications WHERE dev_id = %s AND is_read = 0 ORDER BY created_at DESC"
    cursor.execute(get_notifications_query, (dev_id,))
    notifications = cursor.fetchall()
    # Commit changes to database
    conn.commit()
    # Close database connection
    cursor.close()
    conn.close()

    return render_template('developerdashboard.html', user=user, dfname=dfname, projects=projects, projectss=projectss,
                           bugs3=bugs3, archbugs=archbugs,projectsss=projectsss, notifications=notifications, notification_count=notification_count)


@app.route('/mark_devnotification_read/<int:notification_id>')
def mark_devnotification_read(notification_id):
    # Connect to database
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
    cursor = conn.cursor()

    # Update the notification record in the database
    mark_notification_read_query = "UPDATE developer_notifications SET is_read = 1 WHERE notification_id = %s"
    cursor.execute(mark_notification_read_query, (notification_id,))
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()

    return redirect(url_for('developerdashboard'))

# MANAGE BUGS: FOR DEVELOPER
@app.route('/devbugs.html')
def devbugs():
    # Check if user is logged in
    if 'dev_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM developer WHERE dev_id=%s", (session['dev_id'],))
    user = cursor.fetchone()

    # Get user's name from the database
    cursor.execute("SELECT dfname FROM developer WHERE dev_id=%s", (session['dev_id'],))
    dfname = cursor.fetchone()[0]

    # Get the current date and time
    current_datetime = datetime.now()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_developers pt ON p.project_id = pt.project_id " \
            "WHERE pt.dev_id = %s AND p.deadline > %s"

    # Execute the query with the parameters
    cursor.execute(query, (session['dev_id'], current_datetime,))
    projects = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_developers pt ON p.project_id = pt.project_id " \
            "WHERE pt.dev_id = %s AND p.deadline < %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['dev_id'], current_datetime,))
    projectss = cursor.fetchall()

    dev_id = session.get('dev_id')

    get_bugs4 = "SELECT * FROM bugs b " \
                f" JOIN developer_bugs db ON b.bug_id = db.bug_id WHERE dev_id = {dev_id}"
    cursor.execute(get_bugs4)
    bugs4 = cursor.fetchall()

    return render_template('devbugs.html', user=user, dfname=dfname, projects=projects, projectss=projectss,
                           bugs4=bugs4)


@app.route('/developerbugreport/<int:bug_id>')
def developerbugreport(bug_id):
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()

    # Retrieve bug details from the bugs table in the database

    cursor.execute("SELECT * FROM bugs WHERE bug_id = %s", (bug_id,))
    bug = cursor.fetchone()

    # Retrieve project manager's email from the project_managers table in the database
    # cursor.execute("SELECT * FROM testers WHERE tester_id = %s", (bug[10],))
    # tester = cursor.fetchone()[0]

    query = f"SELECT d.dfname FROM developer d JOIN developer_bugs db ON d.dev_id = db.dev_id JOIN " \
            f"bugs b ON db.bug_id = b.bug_id WHERE b.bug_id = {bug_id}"
    cursor.execute(query)
    dfname = cursor.fetchall()

    query = f"SELECT d.dlname FROM developer d JOIN developer_bugs db ON d.dev_id = db.dev_id JOIN " \
            f"bugs b ON db.bug_id = b.bug_id WHERE b.bug_id = {bug_id}"
    cursor.execute(query)
    dlname = cursor.fetchall()

    query = f"SELECT d.dev_id FROM developer d JOIN developer_bugs db ON d.dev_id = db.dev_id JOIN " \
            f"bugs b ON db.bug_id = b.bug_id WHERE b.bug_id = {bug_id}"
    cursor.execute(query)
    dev_id = cursor.fetchall()

    # Render the bug report form with the retrieved bug details
    return render_template('developerbugreport.html', bug=bug, dfname=dfname, dlname=dlname, dev_id=dev_id)


@app.route('/submit_bug_report', methods=['POST'])
def submit_bug_report():
    if request.method == 'POST':
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='BUGTRACKINGSYSTEM120')
        cursor = conn.cursor()

        # Retrieve bug report form data submitted by the developer
        bug_id = request.form['bug_id']
        bug_title = request.form['bug_title']
        priority = request.form['priority']
        description = request.form['description']
        environment = request.form['environment']
        steps_to_reproduce = request.form['steps_to_reproduce']
        expected_result = request.form['expected_results']
        actual_result = request.form['actual_results']
        attachment = request.files['attachment']
        author_tester_id = request.form['author_tester_id']
        developers_assigned = request.form['developers_assigned']
        incident_type = request.form['incident_type']
        project_title = request.form['project_title']
        bug_created_at = request.form['bug_created_at']
        report_id = ''.join(random.choices(string.digits, k=4))

        data = attachment.read()
        # Encode file data as binary
        encoded_data = mysql.connector.Binary(data)

        # Update the bug_reports table in the database with the new bug report
        cursor.execute(
            "INSERT INTO bug_reports (report_id, project_title, bug_created_at, bug_id, bug_title, priority, description, environment, steps_to_reproduce,"
            " expected_result, actual_result, attachment, author_tester_id, developers_assigned, incident_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (report_id, project_title, bug_created_at, bug_id, bug_title, priority, description, environment,
             steps_to_reproduce, expected_result,
             actual_result, encoded_data, author_tester_id, developers_assigned, incident_type))
        conn.commit()

        dev_id = session.get('dev_id')

        get_dev_name = "SELECT d.dfname FROM developer d " \
                       f" JOIN developer_bugs db ON d.dev_id = db.dev_id WHERE db.bug_id = {bug_id}"
        cursor.execute(get_dev_name)
        dfname = cursor.fetchone()[0]
        cursor.fetchall()

        get_dev_lname = "SELECT d.dlname FROM developer d " \
                        f" JOIN developer_bugs db ON d.dev_id = db.dev_id WHERE db.bug_id = {bug_id}"
        cursor.execute(get_dev_lname)
        dlname = cursor.fetchone()[0]
        cursor.fetchall()

        get_dev_email = "SELECT d.email FROM developer d " \
                        f" JOIN developer_bugs db ON d.dev_id = db.dev_id WHERE db.bug_id = {bug_id}"
        cursor.execute(get_dev_email)
        demail = cursor.fetchone()[0]
        cursor.fetchall()

        # BUG REPORT PDF
        # Generate PDF file with bug report details
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle(f'Bug Report ({bug_id}')

        # Wrap the text within the specified area
        description_lines = textwrap.wrap(description, width=60)
        steps_to_reproduce_lines = textwrap.wrap(steps_to_reproduce, width=60)
        actual_result_lines = textwrap.wrap(actual_result, width=60)
        expected_result_lines = textwrap.wrap(expected_result, width=60)

        pdf.setFont("Helvetica", 12)

        # Draw the wrapped text
        y_coord = 900

        pdf.drawString(100, y_coord, "BUG REPORT")
        pdf.drawString(230, y_coord, "")
        y_coord -= 100

        pdf.drawString(270, y_coord, "BUG REPORT")
        pdf.drawString(270, y_coord, "")
        y_coord -= 40

        pdf.drawString(100, y_coord, f"Below is the bug report for bug ID:{bug_id}")
        y_coord -= 40  # Add some space between the fields

        pdf.drawString(100, y_coord, "Reported by dev:")
        pdf.drawString(230, y_coord, f"{dfname} {dlname}")
        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, y_coord, "Dev Email:")
        pdf.drawString(230, y_coord, f"{demail}")
        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, 900, "Report ID:")
        pdf.drawString(230, 900, str(report_id))
        # y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Priority:")
        pdf.drawString(230, y_coord, str(priority))
        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Bug Title:")
        pdf.drawString(230, y_coord, str(bug_title))
        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Project Title:")
        pdf.drawString(230, y_coord, str(project_title))

        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Description:")
        for line in description_lines:
            pdf.drawString(230, y_coord, line)
            y_coord -= 30

        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, y_coord, "Environment:")
        pdf.drawString(230, y_coord, str(environment))

        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Steps to Reproduce:")
        for line in steps_to_reproduce_lines:
            pdf.drawString(230, y_coord, line)
            y_coord -= 20

        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, y_coord, "Expected Result:")
        for line in expected_result_lines:
            pdf.drawString(230, y_coord, line)
            y_coord -= 20

        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, y_coord, "Actual Result:")
        for line in actual_result_lines:
            pdf.drawString(230, y_coord, line)
            y_coord -= 20

        y_coord -= 20  # Add some space between the fields

        pdf.drawString(100, y_coord, "Developers Assigned:")
        pdf.drawString(230, y_coord, str(developers_assigned))

        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Incident Type:")
        pdf.drawString(230, y_coord, str(incident_type))

        y_coord -= 30  # Add some space between the fields

        pdf.drawString(100, y_coord, "Bug Created At:")
        pdf.drawString(230, y_coord, str(bug_created_at))

        y_coord -= 40  # Add some space between the fields
        pdf.drawString(300, y_coord, "Regards, BuiBui Bug Tracking Team ")
        pdf.save()

        get_email_query = "SELECT p.manager_email FROM projects p" \
                          f" JOIN bugs b ON b.project_id = p.project_id WHERE b.bug_id = {bug_id}"
        cursor.execute(get_email_query)
        manager_email = cursor.fetchone()[0]

        # Add the PDF file as an attachment to the email
        msg = MIMEMultipart()
        msg['From'] = 'buibuibugtracking1.2.0@gmail.com'
        msg['To'] = manager_email
        msg['Subject'] = f'Bug Report (bug_id:{bug_id})'
        msg.attach(MIMEText('Hello, please see attached bug report'))

        part = MIMEBase('application', "octet-stream")
        part.set_payload(buffer.getvalue())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="bug_report.pdf"')
        msg.attach(part)

        # Send the email with the PDF file attachment
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'buibuibugtracking1.2.0@gmail.com'
        smtp_password = 'zfgvqxnaglxlqajc'
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        COMMASPACE = ', '
        smtp_connection.sendmail(msg['From'], COMMASPACE.join([msg['To']]), msg.as_string())
        smtp_connection.quit()

        # Redirect back to the developer dashboard
        return redirect(url_for('developerdashboard'))


"""
    # Get the email of the assigned developer
    get_email_query = "SELECT email FROM project_managers WHERE project_id = %s"
    cursor.execute(get_email_query, (dev_id,))
    manager_email = cursor.fetchone()[0]

    # Send bug report to the project manager's email
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'
    message = Message('New Bug Report')
    msg = MIMEText(message)
    msg['Subject'] = 'A new bug report has been submitted for bug ID ' + bug_id
    msg['From'] = sender_email
    msg['To'] = manager_email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, manager_email, msg.as_string())
    server.quit()
"""


# MANAGER LOGIN
@app.route('/login_manager', methods=['GET', 'POST'])
def login_manager():
    if request.method == 'GET':
        return render_template('managerlogin.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='BUGTRACKINGSYSTEM120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project_managers WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['manager_id'] = user[0]
            return redirect('managerdashboard')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('managerlogin.html', error=error)


@app.route('/managerlogout')
def managerlogout():
    # clear the session data
    session.clear()
    # redirect to the login page
    return redirect(url_for('login_manager'))


# MANAGER DASHBOARD
@app.route('/managerdashboard', methods=['GET', 'POST'])
def managerdashboard():
    # Check if user is logged in
    if 'manager_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM project_managers WHERE manager_id=%s", (session['manager_id'],))
    user = cursor.fetchone()

    manager_id = session.get('manager_id')
    # Get user's name from the database
    cursor.execute("SELECT mfname FROM project_managers WHERE manager_id=%s", (session['manager_id'],))
    mfname = cursor.fetchone()[0]

    # Get the current date and time
    current_datetime = datetime.now()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_projectmanagers pt ON p.project_id = pt.project_id " \
            "WHERE pt.manager_id = %s AND p.deadline > %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['manager_id'], current_datetime,))
    projects = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_projectmanagers pt ON p.project_id = pt.project_id " \
            "WHERE pt.manager_id = %s AND p.deadline < %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['manager_id'], current_datetime,))
    projectss = cursor.fetchall()

    # Get a list of bugs grouped by project title for the logged in manager's projects
    get_bugs = ("SELECT * "
                "FROM bugs "
                "WHERE project_title IN (SELECT project_title FROM projects WHERE project_id "
                "IN (SELECT project_id FROM project_projectmanagers WHERE manager_id = %s)) "
                "ORDER BY project_title")
    cursor.execute(get_bugs, (manager_id,))
    bugs = cursor.fetchall()

    # Construct the SQL query to retrieve the list of developers for each project
    projects_dict = {}
    for project in projects:
        # Get developers for each project
        get_developers = f"SELECT d.* FROM developer d JOIN project_developers " \
                         f"pd ON d.dev_id = pd.dev_id WHERE pd.project_id = {project[0]}"
        # Execute the query with the project_id parameter
        cursor.execute(get_developers)
        developerz = cursor.fetchall()
        projects_dict[project[0]] = developerz

    developer_list = {}
    for bugs in bugs:
        get_developerz = "SELECT d.* FROM developer d JOIN project_developers pd ON d.dev_id = pd.dev_id " \
                         f"WHERE pd.project_id = (SELECT project_id FROM bugs WHERE bug_id = {bugs[0]})"
        # Execute the query with the project_id parameter
        cursor.execute(get_developerz)
        developers = cursor.fetchall()
        developer_list[bugs[0]] = developers

        # Create the dropdown list of developers
        # developer_list = [(dev[0], f"{dev[1]} {dev[2]}") for dev in developers]

    # Get a list of bugs grouped by project title for the logged in manager's projects
    get_bugs2 = ("SELECT * "
                 "FROM bugs "
                 "WHERE project_title IN (SELECT project_title FROM projects WHERE project_id "
                 "IN (SELECT project_id FROM project_projectmanagers WHERE manager_id = %s)) "
                 "AND status IN ('OPEN', 'IN-PROGRESS', 'RESOLVED') "
                 "ORDER BY project_title")
    cursor.execute(get_bugs2, (manager_id,))
    bugs2 = cursor.fetchall()

    # bugs whose status= closed
    archbugs = ("SELECT * "
                 "FROM bugs "
                 "WHERE project_title IN (SELECT project_title FROM projects WHERE project_id "
                 "IN (SELECT project_id FROM project_projectmanagers WHERE manager_id = %s)) "
                 "AND status = 'CLOSED' "
                "ORDER BY project_title")
    cursor.execute(archbugs, (manager_id,))
    archbugs = cursor.fetchall()


    query = "SELECT p.* FROM projects p JOIN project_projectmanagers pt ON p.project_id = pt.project_id " \
            "WHERE pt.manager_id = %s AND p.deadline > %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['manager_id'], current_datetime,))
    projectsss = cursor.fetchall()

    # get developer for each bug
    dev_dict = {}
    for bugs in bugs2:
        # Get developers for the project
        bug_developers = f"SELECT d.* FROM developer d JOIN developer_bugs db ON d.dev_id = db.dev_id " \
                         f"WHERE db.bug_id = {bugs[0]}"
        cursor.execute(bug_developers)
        developerzz = cursor.fetchall()
        dev_dict[bugs[0]] = developerzz

    manager_id = session.get('manager_id')
    # Notification count
    get_notification_count_query = "SELECT COUNT(*) FROM manager_notifications WHERE manager_id = %s AND is_read = 0"
    cursor.execute(get_notification_count_query, (str(manager_id),))
    notification_count = cursor.fetchone()[0]

    # Retrieving notifications for a user
    get_notifications_query = "SELECT * FROM manager_notifications WHERE manager_id = %s AND is_read = 0 ORDER BY created_at DESC"
    cursor.execute(get_notifications_query, (manager_id,))
    notifications = cursor.fetchall()
    # Commit changes to database
    conn.commit()
    # Close database connection
    cursor.close()
    conn.close()

    # Render the manager dashboard with the relevant data
    return render_template('managerdashboard.html', user=user, mfname=mfname, projects=projects, archbugs=archbugs,
                           developer_list=developer_list, bugs2=bugs2, projectsss=projectsss, notifications=notifications, notification_count=notification_count,
                           projectss=projectss, dev_dict=dev_dict, bugs=bugs, projects_dict=projects_dict)


# MANAGE PROJECT
@app.route('/manageproject', methods=['GET', 'POST'])
def manageproject():
    # Check if user is logged in
    if 'manager_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM project_managers WHERE manager_id=%s", (session['manager_id'],))
    user = cursor.fetchone()

    manager_id = session.get('manager_id')
    # Get user's name from the database
    cursor.execute("SELECT mfname FROM project_managers WHERE manager_id=%s", (session['manager_id'],))
    mfname = cursor.fetchone()[0]

    # Get the current date and time
    current_datetime = datetime.now()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_projectmanagers pt ON p.project_id = pt.project_id " \
            "WHERE pt.manager_id = %s AND p.deadline > %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['manager_id'], current_datetime,))
    projects = cursor.fetchall()

    # Construct the SQL query with the restriction on project deadlines
    query = "SELECT p.* FROM projects p JOIN project_projectmanagers pt ON p.project_id = pt.project_id " \
            "WHERE pt.manager_id = %s AND p.deadline < %s"
    # Execute the query with the parameters
    cursor.execute(query, (session['manager_id'], current_datetime,))
    projectss = cursor.fetchall()

    # Get a list of bugs grouped by project title for the logged in manager's projects
    get_bugs = ("SELECT * "
                "FROM bugs "
                "WHERE project_title IN (SELECT project_title FROM projects WHERE project_id "
                "IN (SELECT project_id FROM project_projectmanagers WHERE manager_id = %s)) "
                "ORDER BY project_title")
    cursor.execute(get_bugs, (manager_id,))
    bugs = cursor.fetchall()

    # Construct the SQL query to retrieve the list of developers for each project
    projects_dict = {}
    for project in projects:
        # Get developers for each project
        get_developers = f"SELECT d.* FROM developer d JOIN project_developers " \
                         f"pd ON d.dev_id = pd.dev_id WHERE pd.project_id = {project[0]}"
        # Execute the query with the project_id parameter
        cursor.execute(get_developers)
        developerz = cursor.fetchall()
        projects_dict[project[0]] = developerz

    developer_list = {}
    for bugs in bugs:
        get_developerz = "SELECT d.* FROM developer d JOIN project_developers pd ON d.dev_id = pd.dev_id " \
                         f"WHERE pd.project_id = (SELECT project_id FROM bugs WHERE bug_id = {bugs[0]})"
        # Execute the query with the project_id parameter
        cursor.execute(get_developerz)
        developers = cursor.fetchall()
        developer_list[bugs[0]] = developers

        # Create the dropdown list of developers
        # developer_list = [(dev[0], f"{dev[1]} {dev[2]}") for dev in developers]

    # Get a list of bugs grouped by project title for the logged in manager's projects
    get_bugs77 = ("SELECT * "
                  "FROM bugs "
                  "WHERE status='IN-PROGRESS' "
                  "AND project_title IN "
                  "(SELECT project_title FROM projects WHERE project_id "
                  "IN (SELECT project_id FROM project_projectmanagers WHERE manager_id = %s)) "
                  "ORDER BY project_title")
    cursor.execute(get_bugs77, (manager_id,))
    bugs77 = cursor.fetchall()

    fetch_fixes_query = "SELECT * " \
                        "FROM fixes f JOIN bugs b ON b.bug_id = f.bug_id " \
                        "JOIN projects p ON p.project_id = b.project_id " \
                        "WHERE p.manager_id = %s AND b.status IN ('OPEN', 'IN-PROGRESS', 'RESOLVED')"
    cursor.execute(fetch_fixes_query, (manager_id,))
    fixes_data = cursor.fetchall()

    # get developer for each bug
    dev_dict = {}
    for bugs in bugs77:
        # Get developers for the project
        bug_developers = f"SELECT d.* FROM developer d JOIN developer_bugs db ON d.dev_id = db.dev_id " \
                         f"WHERE db.bug_id = {bugs[0]}"
        cursor.execute(bug_developers)
        developerzz = cursor.fetchall()
        dev_dict[bugs[0]] = developerzz

    # Render the manager dashboard with the relevant data
    return render_template('manageproject.html', user=user, mfname=mfname, projects=projects,
                           developer_list=developer_list, bugs77=bugs77, fixes_data=fixes_data,
                           projectss=projectss, dev_dict=dev_dict, bugs=bugs, projects_dict=projects_dict)


# ASSIGN DEVELOPER TO BUG
@app.route('/assign_developer_to_bug/<int:bug_id>', methods=['GET', 'POST'])
def assign_developer_to_bug(bug_id):
    # Retrieve the manager_id from the session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get the developer_id from the form
        dev_id = request.form.get('dev_id')

        # Add the developer to the developer_bugs table
        insert_query = "INSERT INTO developer_bugs (dev_id, bug_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (dev_id, bug_id))
        conn.commit()

        # Update the status of the bug associated with the developer
        update_status = "UPDATE bugs SET status = 'IN-PROGRESS' WHERE bug_id IN (SELECT bug_id FROM developer_bugs WHERE dev_id = %s)"
        cursor.execute(update_status, (dev_id,))

        # Get the email of the assigned developer
        get_email_query = "SELECT email FROM developer WHERE dev_id = %s"
        cursor.execute(get_email_query, (dev_id,))
        dev_email = cursor.fetchone()[0]

        # Get the title of the bug and the project it belongs to
        get_bug_title_query = "SELECT bug_title FROM bugs WHERE bug_id = %s"
        cursor.execute(get_bug_title_query, (bug_id,))
        bug_title = cursor.fetchone()[0]

        get_project_title_query = "SELECT project_title FROM projects WHERE project_id IN (SELECT project_id FROM bugs WHERE bug_id = %s)"
        cursor.execute(get_project_title_query, (bug_id,))
        project_title = cursor.fetchone()[0]

        # Email the assigned developer
        sender_email = 'buibuibugtracking1.2.0@gmail.com'
        sender_password = 'zfgvqxnaglxlqajc'
        message = f"Hello,\n\nYou have been assigned to bug ID:{bug_id} ({bug_title}) for project: {project_title}.\n\nRegards,\nBuiBui Bug Tracking Team"
        msg = MIMEText(message)
        msg['Subject'] = f"Bug {bug_id} assigned to you"
        msg['From'] = sender_email
        msg['To'] = dev_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, dev_email, msg.as_string())
        server.quit()

        notification_id = ''.join(random.choices(string.digits, k=4))
        get_dev_info_query = "SELECT bugs.project_title, developer_bugs.dev_id FROM bugs INNER JOIN developer_bugs ON bugs.bug_id = developer_bugs.bug_id WHERE bugs.bug_id = %s"
        cursor.execute(get_dev_info_query, (bug_id,))
        dev_info = cursor.fetchone()
        dproject_title = dev_info[0]
        ddev_id = dev_info[1]

        insertt_notification_query = "INSERT INTO developer_notifications (notification_id, dev_id, message, link, bug_id) " \
                                     "VALUES (%s, %s, %s, %s, %s)"

        message = f"Your fix for Bug (ID: {bug_id}) for {dproject_title} is APPROVED"
        link = url_for('developerdashboard')
        values = (notification_id, ddev_id, message, link, bug_id)
        cursor.execute(insertt_notification_query, values)

        flash('Developer assigned to bug successfully', 'success')
        return redirect(url_for('managerdashboard', bug_id=bug_id))

    return render_template('managerdashboard.html')


@app.route('/remove_developer_from_bug/<int:bug_id>', methods=['GET', 'POST'])
def remove_developer_from_bug(bug_id):
    # Retrieve the manager_id from the session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get the developer_id from the form
        dev_id = request.form.get('dev_id')

        # Remove the developer from the developer_bugs table
        remove_query = "DELETE FROM developer_bugs WHERE dev_id = %s AND bug_id = %s;"
        cursor.execute(remove_query, (dev_id, bug_id))
        conn.commit()

        flash('Developer removed from bug successfully', 'success')
        return redirect(url_for('managerdashboard', bug_id=bug_id))

    return render_template('managerdashboard.html')


# TESTER PROFILE DISPLAY
@app.route('/testerprofile')
def testerprofile():
    # Check if user is logged in
    if 'tester_id' not in session:
        return redirect('/testerlogin')

    # Get tester's details from the database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Testers WHERE tester_id=%s", (session['tester_id'],))
    tester = cursor.fetchone()

    return render_template('testerprofile.html', tester=tester)


# DEVELOPER PROFILE DISPLAY
@app.route('/developerprofile')
def developerprofile():
    # Check if user is logged in
    if 'dev_id' not in session:
        return redirect('/developerlogin')

    # Get tester's details from the database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM developer WHERE dev_id=%s", (session['dev_id'],))
    developer = cursor.fetchone()

    return render_template('developerprofile.html', developer=developer)


# MANAGER PROFILE DISPLAY
@app.route('/managerprofile')
def managerprofile():
    # Check if user is logged in
    if 'manager_id' not in session:
        return redirect('/managerlogin')

    # Get tester's details from the database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM project_managers WHERE manager_id=%s", (session['manager_id'],))
    manager = cursor.fetchone()

    return render_template('managerprofile.html', project_managers=manager)


# USERS REPORT ISSUE WITH ALREADY DEPLOYED SYSTEMS
@app.route('/technicalissue', methods=['POST'])
def technicalissue():
    # Get form data
    first_name = request.form['fname']
    user_email = request.form['email']
    software = request.form['software']
    issue = request.form['steps']
    problem = request.form['actual']
    expected_outcome = request.form['expected']
    summary = request.form['summary']
    problem_type = request.form['problem_type']
    # Generate a unique ticket ID
    ticket_id = str(uuid.uuid4())

    # Send email to the technical team
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    techteam_email = 'techteam.buibuibugtracking@gmail.com'
    password = 'zfgvqxnaglxlqajc'
    message = f'Subject: New Support Ticket {ticket_id}\n\n' \
              f'Ticket ID: {ticket_id}\n' \
              f'System: {software}\n' \
              f'Summary: {summary}\n' \
              f'Problem Type: {problem_type}\n' \
              f'Steps Taken: {issue}\n' \
              f'Actual Outcome: {problem}\n' \
              f'Expected Outcome: {expected_outcome}\n' \
              f'User Email: {user_email}\n'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, techteam_email, message)
    # Send email to the user
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    receiver_email = user_email
    password = 'zfgvqxnaglxlqajc'
    message = f'Subject: Support Ticket {ticket_id} Received\n\n' \
              f'Dear {first_name},\n\n' \
              f'We have received your support ticket regarding {software}.\n' \
              f'Thank you for contacting us. Your ticket ID is {ticket_id}. ' \
              f'We will get back to you shortly with a resolution.\n\n' \
              f'Best regards,\n' \
              f'The Support Team'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, message)
    return 'Form submitted successfully!'


@app.route('/testerchangepassword', methods=['GET', 'POST'])
def testerchangepassword():
    if request.method == 'POST':
        # Get form data
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        # Check if user is logged in
        if 'tester_id' not in session:
            return redirect('/login_tester')
        # Get user ID from session
        user_id = session['tester_id']
        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='bugtrackingsystem120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Testers WHERE tester_id=%s", (user_id,))
        user = cursor.fetchone()
        if user:
            # Check password meets requirements
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', new_password):
                error = 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number and one special character (@$!%*?&)'
                return render_template('testerchangepassword.html', error=error)
            # Check new password and confirm password match
            if new_password != confirm_password:
                error2 = 'New password and confirm password do not match'
                return render_template('testerchangepassword.html', error2=error2)
            # Update user password in database
            try:
                cursor.execute("UPDATE testers SET password=%s WHERE tester_id=%s",
                               (new_password, session['tester_id']))
                conn.commit()
            except Exception as e:
                error = str(e)
                return render_template('testerchangepassword.html', error=error)
            # Display success message and redirect to dashboard
            success = 'Password updated successfully'
            return render_template('testerlogin.html', success=success)

        else:
            cursor.execute("SELECT * FROM Testers WHERE tester_id=%s", (user_id,))
            ppassword = cursor.fetchone()
            return render_template('testerchangepassword.html', ppassword=ppassword)

    user_id = session['tester_id']
    # Query database for user
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='bugtrackingsystem120')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Testers WHERE tester_id=%s", (user_id,))
    ppassword = cursor.fetchone()
    # If request method is GET, display the change password form
    return render_template('testerchangepassword.html', ppassword=ppassword)


# DEVELOPER CHANGE PASSWORD
@app.route('/developerchangepassword', methods=['GET', 'POST'])
def developerchangepassword():
    if request.method == 'POST':
        # Get form data
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='bugtrackingsystem120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM developer WHERE dev_id=%s AND password=%s", (session['dev_id'], current_password))
        user = cursor.fetchone()

        if user:
            # Check password meets requirements
            if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password):
                error = 'Password must be at least 8 characters long and contain at least one letter, one number and one special character (@#$%^&+=)'
                return render_template('developerchangepassword.html', error=error)

            # Check new password and confirm password match
            if new_password != confirm_password:
                error = 'New password and confirm password do not match'
                return render_template('developerchangepassword.html', error=error)

            # Update user password in database
            cursor.execute("UPDATE developer SET password=%s WHERE dev_id=%s", (new_password, session['dev_id']))
            conn.commit()

            # Display success message and redirect to dashboard
            success = 'Password updated successfully'
            return render_template('developerdashboard.html', success=success)
        else:
            user_id = session['dev_id']
            cursor.execute("SELECT * FROM developer WHERE dev_id=%s", (user_id,))
            ppassword = cursor.fetchone()
            return render_template('developerlogin.html', ppassword=ppassword)

    user_id = session['dev_id']
    # Query database for user
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='bugtrackingsystem120')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM developer WHERE dev_id=%s", (user_id,))
    ppassword = cursor.fetchone()
    # If request method is GET, display the change password form
    return render_template('developerchangepassword.html', ppassword=ppassword)


# MANAGER CHANGE PASSWORD
@app.route('/managerchangepassword', methods=['GET', 'POST'])
def managerchangepassword():
    if request.method == 'POST':
        # Get form data
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='bugtrackingsystem120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project_managers WHERE manager_id=%s AND password=%s",
                       (session['manager_id'], current_password))
        user = cursor.fetchone()

        if user:
            # Check password meets requirements
            if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password):
                error = 'Password must be at least 8 characters long and contain at least one letter, one number and one special character (@#$%^&+=)'
                return render_template('managerchangepassword.html', error=error)

            # Check new password and confirm password match
            if new_password != confirm_password:
                error = 'New password and confirm password do not match'
                return render_template('managerchangepassword.html', error=error)

            # Update user password in database
            cursor.execute("UPDATE project_managers SET password=%s WHERE manager_id=%s",
                           (new_password, session['manager_id']))
            conn.commit()

            # Display success message and redirect to dashboard
            success = 'Password updated successfully'
            return render_template('managerdashboard.html', success=success)
        else:
            # Display error message and redirect back to change password page
            error = 'Incorrect current password'
            return render_template('managerrchangepassword.html', error=error)

    # If request method is GET, display the change password form
    return render_template('managerchangepassword.html')


# ADMIN MANAGES USERS;

# MANAGE TESTERS
@app.route('/manage_testers')
def manage_testers():
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get all testers from database
    get_testers = ("SELECT * FROM testers")
    cursor.execute(get_testers)
    testers = cursor.fetchall()

    # Get projects for each tester
    projects_dict = {}
    for tester in testers:
        # Get project ids and titles for each tester
        get_projects = f"SELECT p.project_id, p.project_title FROM project_testers pt JOIN projects p ON pt.project_id = p.project_id WHERE pt.tester_id = {tester[0]}"
        cursor.execute(get_projects)
        projects = cursor.fetchall()
        projects_dict[tester[0]] = projects

    # Get all projects from database
    get_projects = ("SELECT * FROM projects")
    cursor.execute(get_projects)
    projectss = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('manage_testers.html', testers=testers, projects_dict=projects_dict, projects=projectss)


# REMOVE TESTER FROM PROJECT
@app.route('/remove_tester_from_project/<int:tester_id>', methods=['GET', 'POST'])
def remove_tester_from_project(tester_id):
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get tester details
    get_tester = f"SELECT * FROM testers WHERE tester_id = {tester_id}"
    cursor.execute(get_tester)
    tester = cursor.fetchone()

    # Get projects for tester
    get_projects = f"SELECT p.project_id, p.project_title FROM project_testers pd JOIN projects p ON pd.project_id = p.project_id WHERE pd.tester_id = {tester_id}"
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    if request.method == 'POST':
        # Get project_id from form data
        project_id = request.form.get('project_id')

        # Remove tester from project
        remove_tester_from_project = f"DELETE FROM project_testers WHERE tester_id = {tester_id} AND project_id = {project_id}"
        cursor.execute(remove_tester_from_project)
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        # Redirect back to manage_developers page
        return redirect(url_for('manage_testers'))

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('manage_developers.html', tester=tester, projects=projects)


# REMOVE TESTER FROM SYSTEM
@app.route('/remove_tester/<int:tester_id>', methods=['GET', 'POST'])
def remove_tester(tester_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get tester information from database
        get_tester = ("SELECT * FROM testers WHERE tester_id=%s")
        cursor.execute(get_tester, (tester_id,))
        tester = cursor.fetchone()

        # Ask for confirmation before deleting tester
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Remove tester from database
                delete_tester = ("DELETE FROM testers WHERE tester_id=%s")
                cursor.execute(delete_tester, (tester_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('manage_testers'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('remove_tester.html', tester=tester)


# ASSIGN TESTER TO PROJECT
@app.route('/assign_tester/<int:tester_id>', methods=['GET', 'POST'])
def assign_tester(tester_id):
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    if request.method == 'POST':
        # Get the project_id from the form
        project_id = request.form['project_id']

        # Add the tester to the selected project
        add_tester_to_project = ("INSERT INTO project_testers (tester_id, project_id) VALUES (%s, %s)")
        cursor.execute(add_tester_to_project, (tester_id, project_id))

        # Update the tester_id column in the projects table
        update_project_tester = (
            "UPDATE projects SET tester_id = "
            "(SELECT GROUP_CONCAT(tester_id) FROM project_testers WHERE project_id = %s) "
            "WHERE project_id = %s"
        )
        cursor.execute(update_project_tester, (project_id, project_id))

        # Update the project_id and project_title fields in the testers table
        update_tester_project = ("UPDATE testers SET project_id = %s, project_title = "
                                 "(SELECT project_title FROM projects WHERE project_id = %s) "
                                 "WHERE tester_id = %s")
        cursor.execute(update_tester_project, (project_id, project_id, tester_id))

        cnx.commit()

        flash('Tester assigned to project successfully', 'success')

    # Get all projects from database
    get_projects = ("SELECT * FROM projects")
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()

    return redirect(url_for('manage_testers', projects=projects))


# MANAGE DEVELOPERS
@app.route('/manage_developers')
def manage_developers():
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get all testers from database
    get_developers = ("SELECT * FROM developer")
    cursor.execute(get_developers)
    developers = cursor.fetchall()

    # Get projects for each tester
    projects_dict = {}
    for developer in developers:
        # Get project ids and titles for each tester
        get_projects = f"SELECT p.project_id, p.project_title FROM project_developers pt JOIN projects p ON pt.project_id = p.project_id WHERE pt.dev_id = {developer[0]}"
        cursor.execute(get_projects)
        projects = cursor.fetchall()
        projects_dict[developer[0]] = projects

    # Get all projects from database
    get_projects = ("SELECT * FROM projects")
    cursor.execute(get_projects)
    projectss = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('manage_developers.html', developers=developers, projects_dict=projects_dict,
                           projects=projectss)


# REMOVE DEVELOPER FROM SYSTEM
@app.route('/remove_developer/<int:dev_id>', methods=['GET', 'POST'])
def remove_developer(dev_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_developer = ("SELECT * FROM developer WHERE dev_id=%s")
        cursor.execute(get_developer, (dev_id,))
        developer = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Remove developer from project_developers table
                remove_dev_from_projects = ("DELETE FROM project_developers WHERE dev_id=%s")
                cursor.execute(remove_dev_from_projects, (dev_id,))
                cnx.commit()

                # Remove developer from developer_bugs table
                remove_dev_from_bug = ("DELETE FROM developer_bugs WHERE dev_id=%s")
                cursor.execute(remove_dev_from_bug, (dev_id,))
                cnx.commit()

                # Remove developer from developer table
                delete_developer = ("DELETE FROM developer WHERE dev_id=%s")
                cursor.execute(delete_developer, (dev_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('manage_developers'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('remove_developer.html', developer=developer)


# MANAGE MANAGERS
@app.route('/manage_managers')
def manage_managers():
    # Connect to MySQL
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()
    # Retrieve all the project managers from the database
    cursor.execute("SELECT * FROM project_managers")
    managers = cursor.fetchall()

    # Get projects for each manager
    projects_dict = {}
    for manager in managers:
        # Get project ids and titles for each manager
        get_projects = f"SELECT project_id, project_title FROM projects " \
                       f"WHERE manager_id = {manager[0]}"
        cursor.execute(get_projects)
        projects = cursor.fetchall()
        projects_dict[manager[0]] = projects

    # Get all projects from database
    get_projects = ("SELECT * FROM projects")
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()
    # Render the HTML template with the managers' information
    return render_template('manage_managers.html', managers=managers, projects=projects, projects_dict=projects_dict)


# REMOVE MANAGER FROM SYSTEM
@app.route('/remove_manager/<int:manager_id>', methods=['GET', 'POST'])
def remove_manager(manager_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get tester information from database
        get_manager = ("SELECT * FROM project_managers WHERE manager_id=%s")
        cursor.execute(get_manager, (manager_id,))
        manager = cursor.fetchone()

        # Ask for confirmation before deleting tester
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Remove tester from database
                delete_manager = ("DELETE FROM project_managers WHERE manager_id=%s")
                cursor.execute(delete_manager, (manager_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('manage_managers'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('remove_manager.html', manager=manager)


# ASSIGN DEVELOPER TO PROJECT
@app.route('/assign_developer/<int:dev_id>', methods=['GET', 'POST'])
def assign_developer(dev_id):
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    if request.method == 'POST':
        # Get the project_id from the form
        project_id = request.form['project_id']

        # Add the tester to the selected project
        add_developer_to_project = ("INSERT INTO project_developers (dev_id, project_id) VALUES (%s, %s)")
        cursor.execute(add_developer_to_project, (dev_id, project_id))

        # Update the tester_id column in the projects table
        update_project_developer = (
            "UPDATE projects SET dev_id = "
            "(SELECT GROUP_CONCAT(dev_id) FROM project_developers WHERE project_id = %s) "
            "WHERE project_id = %s"
        )
        cursor.execute(update_project_developer, (project_id, project_id))

        # Update the project_id and project_title fields in the testers table
        update_developer_project = ("UPDATE developer SET project_id = %s, project_title = "
                                    "(SELECT project_title FROM projects WHERE project_id = %s) "
                                    "WHERE dev_id = %s")
        cursor.execute(update_developer_project, (project_id, project_id, dev_id))

        cnx.commit()

        flash('Developer assigned to project successfully', 'success')

    # Get all projects from database
    get_projects = ("SELECT * FROM projects")
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()

    return redirect(url_for('manage_developers', projects=projects))


# ASSIGN MANAGER TO PROJECT
@app.route('/assign_manager/<int:project_id>', methods=['GET', 'POST'])
def assign_manager(project_id):
    if request.method == 'POST':
        # Get the selected manager ID from the form
        manager_id = request.form['manager_id']

        # Connect to the database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Check if the project already has a manager assigned
        check_existing = ("SELECT * FROM project_projectmanagers WHERE project_id = %s")
        cursor.execute(check_existing, (project_id,))
        existing_manager = cursor.fetchone()

        if existing_manager:
            # Update the manager_id of the existing project-manager relationship
            update_relationship = ("UPDATE project_projectmanagers SET manager_id = %s WHERE project_id = %s")
            cursor.execute(update_relationship, (manager_id, project_id))
        else:
            # Add the manager to the selected project
            add_manager_to_project = ("INSERT INTO project_projectmanagers (manager_id , project_id) VALUES (%s, %s)")
            cursor.execute(add_manager_to_project, (manager_id, project_id))

        # Update the project's manager information
        update_project = (
            "UPDATE projects SET manager_id = %s, manager_email = (SELECT email FROM project_managers WHERE manager_id = %s) WHERE project_id = %s")
        cursor.execute(update_project, (manager_id, manager_id, project_id))
        cnx.commit()

        # Close the database connection
        cursor.close()
        cnx.close()

        # Redirect to the current projects page
        return redirect(url_for('currentprojects'))

    else:
        # Connect to the database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get a list of all project managers
        get_managers = ("SELECT * FROM project_managers")
        cursor.execute(get_managers)
        managers = cursor.fetchall()

        # Close the database connection
        cursor.close()
        cnx.close()

        # Render the form with the list of managers
        return render_template('currentprojects.html', managers=managers)


# REMOVE DEVELOPER FROM PROJECT
@app.route('/remove_developer_from_project/<int:dev_id>', methods=['GET', 'POST'])
def remove_developer_from_project(dev_id):
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get developer details
    get_dev = f"SELECT * FROM developer WHERE dev_id = {dev_id}"
    cursor.execute(get_dev)
    developer = cursor.fetchone()

    # Get projects for developer
    get_projects = f"SELECT p.project_id, p.project_title FROM project_developers pd JOIN projects p ON pd.project_id = p.project_id WHERE pd.dev_id = {dev_id}"
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    if request.method == 'POST':
        # Get project_id from form data
        project_id = request.form.get('project_id')

        # Remove developer from project
        remove_dev_from_project = f"DELETE FROM project_developers WHERE dev_id = {dev_id} AND project_id = {project_id}"
        cursor.execute(remove_dev_from_project)
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        # Redirect back to manage_developers page
        return redirect(url_for('manage_developers'))

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('manage_developers.html', developer=developer, projects=projects)


def send_email(to, subject, body, attachment=None):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587  # TLS port
    sender_email = 'buibuibugtracking1.2.0@gmail.com'
    sender_password = 'zfgvqxnaglxlqajc'

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject

    # Add the body to the email message
    message.attach(MIMEText(body, "plain"))

    # Add the attachment to the email message, if any
    if attachment is not None:
        with open(attachment, "rb") as file:
            part = MIMEApplication(file.read(), Name=attachment)
        part['Content-Disposition'] = f'attachment; filename="{attachment}"'
        message.attach(part)

    # Send the email message
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, message.as_string())


# REMOVE MANAGER FROM PROJECT
@app.route('/remove_manager_from_project/<int:manager_id>', methods=['GET', 'POST'])
def remove_manager_from_project(manager_id):
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    get_manager = ("SELECT * FROM project_managers WHERE manager_id = %s")
    cursor.execute(get_manager, (manager_id,))
    manager = cursor.fetchone()

    # Get all projects assigned to the manager
    get_manager_projects = ("SELECT * FROM projects WHERE project_id IN "
                            "(SELECT project_id FROM project_managers WHERE manager_id = %s)")
    cursor.execute(get_manager_projects, (manager_id,))
    projects = cursor.fetchall()

    if request.method == 'POST':
        # Get project_id from form data
        project_id = request.form.get('project_id')

        # Remove project manager from project
        remove_manager = (
            "UPDATE projects SET manager_id = NULL, manager_email = NULL WHERE manager_id = %s AND project_id = %s")
        cursor.execute(remove_manager, (manager_id, project_id))
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        # Redirect back to manage_managers page
        return redirect(url_for('manage_managers'))

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('remove_manager_from_project.html', manager=manager, projects=projects)


# CURRENT PROJECTS
@app.route('/currentprojects')
def currentprojects():
    # Connect to the database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get all projects from the projects table
    get_projects = "SELECT * FROM projects"
    cursor.execute(get_projects)
    projects = cursor.fetchall()

    # Get all projects from database
    get_managers = ("SELECT * FROM project_managers")
    cursor.execute(get_managers)
    managers = cursor.fetchall()

    # Close the database connection
    cursor.close()
    cnx.close()

    return render_template('currentprojects.html', projects=projects, managers=managers)


# DELETE PROJECT FROM SYSTEM
@app.route('/remove_project/<int:project_id>', methods=['GET', 'POST'])
def remove_project(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_project = ("SELECT * FROM projects WHERE project_id=%s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Remove project from project_developers table
                remove_project_from_projectdevelopers = ("DELETE FROM project_developers WHERE project_id=%s")
                cursor.execute(remove_project_from_projectdevelopers, (project_id,))
                cnx.commit()

                # Remove project from project_testers table
                remove_project_from_projecttesters = ("DELETE FROM project_testers WHERE project_id=%s")
                cursor.execute(remove_project_from_projecttesters, (project_id,))
                cnx.commit()

                # Remove project from projects table
                delete_project = ("DELETE FROM projects WHERE project_id=%s")
                cursor.execute(delete_project, (project_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('currentprojects'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('delete_project.html', project=project)


# HALT PROJECT BY ADMIN
@app.route('/halt_project/<int:project_id>', methods=['GET', 'POST'])
def halt_project(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_project = ("SELECT * FROM projects WHERE project_id=%s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Update project status to halted
                update_project = ("UPDATE projects SET project_status = 'halted' WHERE project_id = %s")
                cursor.execute(update_project, (project_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('currentprojects'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('halt_project.html', project=project)


# HALT PROJECT BY PROJECT MANAGER
@app.route('/halt_project_bymanager/<int:project_id>', methods=['GET', 'POST'])
def halt_project_bymanager(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_project = ("SELECT * FROM projects WHERE project_id=%s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Update project status to halted
                update_project = ("UPDATE projects SET project_status = 'halted' WHERE project_id = %s")
                cursor.execute(update_project, (project_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('managerdashboard'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('halt_project_bymanager.html', project=project)


# RESUME PROJECT BY ADMIN
@app.route('/resume_project/<int:project_id>', methods=['GET', 'POST'])
def resume_project(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_project = ("SELECT * FROM projects WHERE project_id=%s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Update project status to halted
                update_project = ("UPDATE projects SET project_status = 'running' WHERE project_id = %s")
                cursor.execute(update_project, (project_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('currentprojects'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('resume_project.html', project=project)


# RESUME PROJECT BY MANAGER
@app.route('/resume_project_bymanager/<int:project_id>', methods=['GET', 'POST'])
def resume_project_bymanager(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get developer information from database
        get_project = ("SELECT * FROM projects WHERE project_id=%s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Ask for confirmation before deleting developer
        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                # Update project status to halted
                update_project = ("UPDATE projects SET project_status = 'running' WHERE project_id = %s")
                cursor.execute(update_project, (project_id,))
                cnx.commit()

                # Close database connection
                cursor.close()
                cnx.close()

                return redirect(url_for('managerdashboard'))

        # Close database connection
        cursor.close()
        cnx.close()

        return render_template('resume_project_bymanager.html', project=project)


# CHANGE DEADLINE OF A PROJECT BY ADMIN
@app.route('/change_deadline/<int:project_id>', methods=['GET', 'POST'])
def change_deadline(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get project by ID
        get_project = ("SELECT * FROM projects WHERE project_id = %s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Get new deadline from form
        new_deadline = request.form['new_deadline']

        # Update project in database
        update_project = ("UPDATE projects SET deadline = %s WHERE project_id = %s")
        cursor.execute(update_project, (new_deadline, project_id))
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('currentprojects'))

    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get project by ID
    get_project = ("SELECT * FROM projects WHERE project_id = %s")
    cursor.execute(get_project, (project_id,))
    project = cursor.fetchone()

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('currentprojects.html', project=project)


# CHANGE DEADLINE OF A PROJECT BY PROJECT MANAGER
@app.route('/managerchange_deadline/<int:project_id>', methods=['GET', 'POST'])
def managerchange_deadline(project_id):
    if request.method == 'POST':
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Get project by ID
        get_project = ("SELECT * FROM projects WHERE project_id = %s")
        cursor.execute(get_project, (project_id,))
        project = cursor.fetchone()

        # Get new deadline from form
        new_deadline = request.form['new_deadline']

        # Update project in database
        update_project = ("UPDATE projects SET deadline = %s WHERE project_id = %s")
        cursor.execute(update_project, (new_deadline, project_id))
        update_status = "UPDATE projects SET project_status = 'HALTED' WHERE deadline IN (SELECT deadline FROM projects WHERE project_id = %s)"
        cursor.execute(update_status, (project_id,))
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('managerdashboard'))

    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get project by ID
    get_project = ("SELECT * FROM projects WHERE project_id = %s")
    cursor.execute(get_project, (project_id,))
    project = cursor.fetchone()

    # Close database connection
    cursor.close()
    cnx.close()

    return render_template('managerdashboard.html', project=project)


# CURRENT BUGS DASHBOARD
@app.route('/currentbugs')
def currentbugs():
    # Connect to database
    cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                  database='bugtrackingsystem120')
    cursor = cnx.cursor()

    # Get bugs with edit_status values
    get_bugs_query = ("SELECT * FROM bugs")
    cursor.execute(get_bugs_query)
    bugs = cursor.fetchall()

    # Close database connection
    cursor.close()
    cnx.close()

    # Render admin dashboard template with bugs and status options
    return render_template('currentbugs.html', bugs=bugs, )


# EDIT BUG PRIORITY BY ADMIN
@app.route('/editbugpriority', methods=['GET', 'POST'])
def editbugpriority():
    if request.method == 'POST':
        # Get form data
        bug_id = request.form['bug_id']
        new_priority = request.form['new_priority']

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Update status in the database
        update_bug_priority = "UPDATE bugs SET priority = %s WHERE bug_id = %s"
        cursor.execute(update_bug_priority, (new_priority, bug_id))

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('currentbugs'))

    else:
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Fetch all bugs from the database
        get_all_bugs = "SELECT * FROM bugs"
        cursor.execute(get_all_bugs)
        bugs = cursor.fetchall()

        # Close database connection
        cursor.close()
        cnx.close()

        # Render the admin dashboard template with the bug data
        return render_template('currentbugs.html', bugs=bugs)


# EDIT BUG PRIORITY BY PROJECT MANAGER
@app.route('/managereditbugpriority', methods=['GET', 'POST'])
def managereditbugpriority():
    if request.method == 'POST':
        # Get form data
        bug_id = request.form['bug_id']
        new_priority = request.form['new_priority']

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Update status in the database
        update_bug_priority = "UPDATE bugs SET priority = %s WHERE bug_id = %s"
        cursor.execute(update_bug_priority, (new_priority, bug_id))

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('managerdashboard'))

    else:
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Fetch all bugs from the database
        get_all_bugs = "SELECT * FROM bugs"
        cursor.execute(get_all_bugs)
        bugs = cursor.fetchall()

        # Close database connection
        cursor.close()
        cnx.close()

        # Render the admin dashboard template with the bug data
        return render_template('managerdashboard.html', bugs=bugs)


# EDIT BUG STATUS BY ADMIN
@app.route('/editbugstatus', methods=['GET', 'POST'])
def editbugstatus():
    if request.method == 'POST':
        # Get form data
        bug_id = request.form['bug_id']
        new_status = request.form['new_status']

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Update status in the database
        update_bug_status = "UPDATE bugs SET status = %s WHERE bug_id = %s"
        cursor.execute(update_bug_status, (new_status, bug_id))

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('currentbugs'))

    else:
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Fetch all bugs from the database
        get_all_bugs = "SELECT * FROM bugs"
        cursor.execute(get_all_bugs)
        bugs = cursor.fetchall()

        # Close database connection
        cursor.close()
        cnx.close()

        # Render the admin dashboard template with the bug data
        return render_template('currentbugs.html', bugs=bugs)


# EDIT BUG STATUS BY PROJECT MANAGER
@app.route('/managereditbugstatus', methods=['GET', 'POST'])
def managereditbugstatus():
    if request.method == 'POST':
        # Get form data
        bug_id = request.form['bug_id']
        new_status = request.form['new_status']

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Update status in the database
        update_bug_status = "UPDATE bugs SET status = %s WHERE bug_id = %s"
        cursor.execute(update_bug_status, (new_status, bug_id))

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('managerdashboard'))

    else:
        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Fetch all bugs from the database
        get_all_bugs = "SELECT * FROM bugs"
        cursor.execute(get_all_bugs)
        bugs = cursor.fetchall()

        # Close database connection
        cursor.close()
        cnx.close()

        # Render the admin dashboard template with the bug data
        return render_template('managerdashboard.html', bugs=bugs)


# APPROVE/DENY FIX BY PROJECT MANAGER
@app.route('/approvebugstatus', methods=['GET', 'POST'])
def approvebugstatus():
    if request.method == 'POST':
        # Get form data
        bug_id = request.form['bug_id']
        new_status = request.form['new_status']

        # Connect to database
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        # Update status in the database
        update_bug_status = "UPDATE bugs SET status = %s WHERE bug_id = %s"
        cursor.execute(update_bug_status, (new_status, bug_id))

        if new_status == 'CLOSED':
            notification_id = ''.join(random.choices(string.digits, k=4))

            get_bug_info_query = "SELECT b.project_title, b.tester_id FROM bugs b WHERE b.bug_id = %s"
            cursor.execute(get_bug_info_query, (bug_id,))
            bug_info = cursor.fetchone()
            project_title = bug_info[0]
            tester_id = bug_info[1]

            insert_notification_query = "INSERT INTO tester_notifications (notification_id, tester_id, message, link, bug_status, bug_id) " \
                                        "VALUES (%s, %s, %s, %s, %s, %s)"

            message = f"Bug (ID: {bug_id}) for {project_title} has been fixed"
            link = url_for('testerdashboard')
            bug_status = "CLOSED"
            values = (notification_id, tester_id, message, link, bug_status, bug_id)
            cursor.execute(insert_notification_query, values)

            get_dev_info_query = "SELECT bugs.project_title, developer_bugs.dev_id FROM bugs INNER JOIN developer_bugs ON bugs.bug_id = developer_bugs.bug_id WHERE bugs.bug_id = %s"
            cursor.execute(get_dev_info_query, (bug_id,))
            dev_info = cursor.fetchone()
            dproject_title = dev_info[0]
            dev_id = dev_info[1]

            insertt_notification_query = "INSERT INTO developer_notifications (notification_id, dev_id, message, link, bug_status, bug_id) " \
                                        "VALUES (%s, %s, %s, %s, %s, %s)"

            message = f"Your fix for Bug (ID: {bug_id}) for {dproject_title} is APPROVED"
            link = url_for('developerdashboard')
            bug_status = "CLOSED"
            values = (notification_id, dev_id, message, link, bug_status, bug_id)
            cursor.execute(insertt_notification_query, values)

        else:
            notification_id = ''.join(random.choices(string.digits, k=4))

            get_dev_info_query = "SELECT bugs.project_title, developer_bugs.dev_id FROM bugs INNER JOIN developer_bugs ON bugs.bug_id = developer_bugs.bug_id WHERE bugs.bug_id = %s"
            cursor.execute(get_dev_info_query, (bug_id,))
            dev_info = cursor.fetchone()
            dproject_title = dev_info[0]
            dev_id = dev_info[1]

            insertt_notification_query = "INSERT INTO developer_notifications (notification_id, dev_id, message, link, bug_status, bug_id) " \
                                         "VALUES (%s, %s, %s, %s, %s, %s)"

            message = f"Your fix for Bug (ID: {bug_id}) for {dproject_title} is DENIED"
            link = url_for('developerdashboard')
            bug_status = "OPEN"
            values = (notification_id, dev_id, message, link, bug_status, bug_id)
            cursor.execute(insertt_notification_query, values)

        # Commit changes to database
        cnx.commit()

        # Close database connection
        cursor.close()
        cnx.close()

        return redirect(url_for('manageproject'))


# DEVELOPER SENDS PULL REQUEST
# Import datetime module to get current timestamp
@app.route('/approval/<int:bug_id>', methods=['POST'])
def approval(bug_id):
    if request.method == 'POST':
        confirmation = request.form.get('confirmation')
        if confirmation == 'yes':
            # Connect to MySQL database
            cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                          database='bugtrackingsystem120')
            cursor = cnx.cursor()

            # Get developer ID from session
            dev_id = session.get('dev_id')
            id = ''.join(random.choices(string.digits, k=4))

            # Get project title and tester ID from bugs table using bug ID
            get_bug_info_query = "SELECT b.project_title, b.tester_id FROM bugs b WHERE b.bug_id = %s"
            cursor.execute(get_bug_info_query, (bug_id,))
            bug_info = cursor.fetchone()
            project_title = bug_info[0]
            tester_id = bug_info[1]

            # Insert data into fixes table
            insert_fix_query = "INSERT INTO fixes (id, dev_id, bug_id, project_title, tester_id) " \
                               "VALUES (%s, %s, %s, %s, %s)"
            data = (id, dev_id, bug_id, project_title, tester_id)
            cursor.execute(insert_fix_query, data)
            cnx.commit()

            # Send email with login details
            subject = 'Bug Fix Approval Request'
            body = f"Bug #{bug_id} has been fixed and is pending approval.\n Developer ID: {dev_id}"
            sender_email = 'buibuibugtracking1.2.0@gmail.com'
            sender_password = 'zfgvqxnaglxlqajc'
            recipient_email_query = "SELECT p.manager_email FROM projects p " \
                                    "JOIN bugs b ON b.project_id = p.project_id WHERE b.bug_id = %s"
            cursor.execute(recipient_email_query, (bug_id,))
            manager_email = cursor.fetchone()[0]

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(sender_email, sender_password)
                smtp.sendmail(sender_email, manager_email, f'Subject: {subject}\n\n{body}')

            notification_id = ''.join(random.choices(string.digits, k=4))
            get_manager_info_query = "SELECT projects.project_title, projects.manager_id FROM bugs INNER JOIN projects ON bugs.project_title = projects.project_title WHERE bugs.bug_id = %s"
            cursor.execute(get_manager_info_query, (bug_id,))
            manager_info = cursor.fetchone()
            mproject_title = manager_info[0]
            manager_id = manager_info[1]

            insertt_notification_query = "INSERT INTO manager_notifications (notification_id, manager_id, message, link, bug_id) " \
                                         "VALUES (%s, %s, %s, %s, %s)"

            message = f"Pending Fix Approval for Bug (ID: {bug_id}) for {mproject_title} "
            link = url_for('manageproject')
            values = (notification_id, manager_id, message, link, bug_id)
            cursor.execute(insertt_notification_query, values)
            cnx.commit()

            # Close database connection and redirect to developer dashboard
            cursor.close()
            cnx.close()
            return redirect(url_for('developerdashboard'))

    return render_template('approval.html')


# EDIT BUG STATUS BY DEVELOPER
@app.route('/developereditbugstatus/<int:bug_id>', methods=['GET', 'POST'])
def developereditbugstatus(bug_id):
    if request.method == 'POST':
        cnx = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                      database='bugtrackingsystem120')
        cursor = cnx.cursor()

        dev_id = session.get('dev_id')

        get_bugs = ("SELECT * "
                    "FROM bugs "
                    "WHERE project_title IN (SELECT project_title FROM projects WHERE project_id "
                    "IN (SELECT project_id FROM project_developers WHERE dev_id = %s)) "
                    "ORDER BY project_title")
        cursor.execute(get_bugs, (dev_id,))
        bugs = cursor.fetchall()

        if request.method == 'POST':
            confirmation = request.form.get('confirmation')
            if confirmation == 'yes':
                update_bug_status = ("UPDATE bugs SET status = 'RESOLVED' WHERE bug_id = %s")
                cursor.execute(update_bug_status, (bug_id,))

                # Commit changes to database
                cnx.commit()
                cursor.close()

                return redirect(url_for('developerdashboard'))
                # Close database connection
        cursor.close()
        cnx.close()

        return render_template('editstatus.html', bugs=bugs)


# ADMIN LOGIN
@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'GET':
        return render_template('adminlogin.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='BUGTRACKINGSYSTEM120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['admin_id'] = user[0]
            return redirect('/admindashboard')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('adminlogin.html', error=error)


@app.route('/adminlogout')
def adminlogout():
    # clear the session data
    session.clear()
    # redirect to the login page
    return redirect(url_for('login_admin'))



@app.route('/admindashboard')
def admindashboard():
    # Check if user is logged in
    if 'admin_id' not in session:
        return redirect('/')

    # Get user from database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE admin_id=%s", (session['admin_id'],))
    user = cursor.fetchone()

    # Get user's name from the database
    cursor.execute("SELECT afname FROM admin WHERE admin_id=%s", (session['admin_id'],))
    afname = cursor.fetchone()[0]

    return render_template('admin.html', user=user, afname=afname)


# ADMIN PROFILE DISPLAY
@app.route('/adminprofile')
def adminprofile():
    # Check if user is logged in
    if 'admin_id' not in session:
        return redirect('/adminlogin')

    # Get tester's details from the database using their ID stored in session
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='BUGTRACKINGSYSTEM120')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE admin_id=%s", (session['admin_id'],))
    admin = cursor.fetchone()

    return render_template('adminprofile.html', admin=admin)


# ADMIN CHANGE PASSWORD
@app.route('/adminchangepassword', methods=['GET', 'POST'])
def adminchangepassword():
    if request.method == 'POST':
        # Get form data
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Query database for user
        conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                       database='bugtrackingsystem120')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE admin_id=%s AND password=%s",
                       (session['admin_id'], current_password))
        user = cursor.fetchone()

        if user:
            # Check password meets requirements
            if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password):
                error = 'Password must be at least 8 characters long and contain at least one letter, one number and one special character (@#$%^&+=)'
                return render_template('adminchangepassword.html', error=error)

            # Check new password and confirm password match
            if new_password != confirm_password:
                error = 'New password and confirm password do not match'
                return render_template('adminchangepassword.html', error=error)

            # Update user password in database
            cursor.execute("UPDATE admin SET password=%s WHERE admin_id=%s",
                           (new_password, session['admin_id']))
            conn.commit()

            # Display success message and redirect to dashboard
            success = 'Password updated successfully'
            return render_template('admin.html', success=success)
        else:
            # Display error message and redirect back to change password page
            error = 'Incorrect current password'
            return render_template('adminchangepassword.html', error=error)

    # If request method is GET, display the change password form
    return render_template('adminchangepassword.html')


# SEARCH FOR EXISTING BUG
@app.route('/search')
def search():
    bug_status = request.args.get('bug_status')
    project_title = request.args.get('project_title')
    search_term = request.args.get('search_term')

    # Query database for user
    conn = mysql.connector.connect(user='bethlydia', password='aVOCADO999!', host='localhost',
                                   database='bugtrackingsystem120')
    cursor = conn.cursor()

    tester_id = session.get('tester_id')

    get_tester_projects = "SELECT p.project_id, p.project_title FROM project_testers pt JOIN projects p ON pt.project_id = p.project_id WHERE pt.tester_id = %s"
    cursor.execute(get_tester_projects, (tester_id,))
    projectss = cursor.fetchall()

    # Search for bugs matching search terms
    query = "SELECT * FROM bugs WHERE status=%s AND project_title=%s AND (bug_title LIKE %s OR bug_description LIKE %s OR actual_results LIKE %s OR expected_results LIKE %s)"
    search_term = '%' + search_term + '%'
    cursor.execute(query, (bug_status, project_title, search_term, search_term, search_term, search_term))
    bugs = cursor.fetchall()

    # Close the database connection and return the results
    cursor.close()
    return render_template('search_results.html', bugs=bugs, projects=projectss, search_term=search_term)


if __name__ == '__main__':
    app.run(debug=True)
