# system_admin.py
from flask import Flask, request, render_template
import db as db_func
from flask_sqlalchemy import SQLAlchemy
from main import Testers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bethlydia:aVOCADO999!@localhost/bugtrackingsystem120'
db = SQLAlchemy(app)

"""
def __repr__(self):
    return '<Testers %r>' % self.name
"""


@app.route("/admin")
def system_admin():
    return render_template("admin.html")


@app.route("/add_tester", methods=["GET", "POST"])
def add_tester():
    # print('Received request:', request.method, request.form)
    if request.method == "POST":
        name = request.form["Tname"]
        email = request.form["Temail"]
        password = request.form["Tpassword"]
        print(name, email, password)
        tester = Testers(name=name, email=email, password=password)  # DO THIS FOR OTHER FUNC!!!!!!
        db.session.add(tester)
        db.session.commit()
        # db_func.add_tester(name, email, password)
        return "Tester added successfully"
    return render_template("add_tester.html")


@app.route("/add_developer", methods=["POST"])
def add_developer():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    db_func.add_developer(name, email, password)
    return "Developer added successfully"


@app.route("/add_project_manager", methods=["POST"])
def add_project_manager():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    db_func.add_project_manager(name, email, password)
    return "Project Manager added successfully"


@app.route("/assign_project_manager", methods=["POST"])
def assign_project_manager():
    project_id = request.form["project_id"]
    project_manager_email = request.form["project_manager_email"]
    db_func.assign_project_manager(project_id, project_manager_email)
    return "Project Manager assigned to project successfully"


@app.route("/view_all_projects")
def view_all_projects():
    projects = db_func.get_all_projects()
    return render_template("view_all_projects.html", projects=projects)


@app.route("/view_all_bugs")
def view_all_bugs():
    bugs = db_func.get_all_bugs()
    return render_template("view_all_bugs.html", bugs=bugs)


@app.route("/assign_tester", methods=["POST"])
def assign_tester():
    tester_email = request.form["tester_email"]
    project_id = request.form["project_id"]
    db_func.assign_tester(tester_email, project_id)
    return "Tester assigned to project successfully"


if __name__ == "__main__":
    app.run(debug=True)
