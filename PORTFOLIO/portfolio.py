from ast import Return
from django.shortcuts import render
from flask import Flask,render_template,flash,redirect,url_for



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/certificates")
def certificates():
    return render_template("my_certificates.html")

@app.route("/articles")
def articles(): 
    return render_template("articles.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")



if __name__ == "__main__":
    app.run(debug=True)
