
import mysql.connector
from flask import app, Flask
from flask_sqlalchemy import SQLAlchemy
from main import db
from main import Testers, ProjectManagers, Developer
from app.bug import db

app = Flask(__name__)
db = SQLAlchemy


def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="bethlydia",
        password="aVOCADO999!",
        database="bugtrackingsystem120"
    )
    return conn


def add_tester(name, email, password):
    tester = Testers.query.filter_by(name=name).first()
    tester.email = email
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO tester (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    conn.commit()
    print("Tester added successfully!")


def add_developer(name, email, password):
    developer = Developer.query.filter_by(name=name).first()
    developer.email = email
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO developer (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    conn.commit()
    print("Developer added successfully!")


def add_project_manager(name, email, password):
    manager = ProjectManagers.query.filter_by(name=name).first()
    manager.email = email
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO project_manager (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    conn.commit()
    print("Project Manager added successfully!")


def assign_project_manager(project_id, project_manager_id):
    manager = ProjectManagers.query.filter_by(project_id=project_id).first()
    manager.manager_id = project_manager_id
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE project SET project_manager_id = %s WHERE id = %s"
    values = (project_manager_id, project_id)
    cursor.execute(query, values)
    conn.commit()
    print("Project Manager assigned successfully!")


def view_all_projects():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM project"
    cursor.execute(query)
    projects = cursor.fetchall()
    print("Project ID | Project Name | Project Manager ID")
    for project in projects:
        print(project[0], " | ", project[1], " | ", project[2])


def view_all_bugs():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM bug"
    cursor.execute(query)
    bugs = cursor.fetchall()
    print("Bug ID | Bug Name | Project ID | Tester ID")
    for bug in bugs:
        print(bug[0], " | ", bug[1], " | ", bug[2], " | ", bug[3])


def assign_tester(tester_id, project_id):
    tester = Testers.query.filter_by(tester_id=tester_id).first()
    tester.project_id = project_id
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO tester_project (tester_id, project_id) VALUES (%s, %s)"
    values = (tester_id, project_id)
    cursor.execute(query, values)
    conn.commit()
    print("Tester assigned successfully!")


if __name__ == "__main__":
    app.run(debug=True)
