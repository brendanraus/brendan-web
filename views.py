import logging
from flask import Flask, Blueprint, render_template

views = Blueprint("views", __name__)

# basic logging
logging.basicConfig(level=logging.DEBUG)

# Route for Home 
@views.route("/home")
def home():
    logging.debug("Rendering the index.html template")
    return render_template("index.html")

# Route for About
@views.route("/about")
def about():
    logging.debug("Rendering the about.html template")
    return render_template("about.html")

# Route for Projects
@views.route("/projects")
def projects():
    logging.debug("Rendering the projects.html template")
    return render_template("projects.html")

# Route for Productivity 
@views.route("/productivity")
def productivity():
    logging.debug("Rendering the projects.html template")
    return render_template("productivity.html")

# Route for Services
@views.route("/services")
def services():
    logging.debug("Rendering the projects.html template")
    return render_template("services.html")

# Route for Contact
@views.route("/contact")
def contact():
    logging.debug("Rendering the contact.html template")
    return render_template("contact.html")












