
# we will keep the routes and functionalities here separately
# to know what is used as "app" and "render_template" 
# we will import them from app.py module
from app import app, db
from flask import render_template, redirect, url_for

# import our forms
import forms

# import Task class
from models import Task
from datetime import datetime


# we will define routes to make the app capable of hosting different url sites
# we can return text/html and other values such as JSON as return value of a route
# we will use decorators to tell our server that we want to run the function 
# defined below to be run at the specified url path
@app.route('/')          # we can use multiple routes with the same function
@app.route('/index')     # the index folder
def index():
    # list the tasks that are on our database
    tasks = Task.query.all()

    #returns html value forthe GET request at /index page and / page
    #return '<h1>Hello</h1> World!'
    # return the html content from an html file with specific variable (tasks) values 
    return render_template('index.html', tasks=tasks)


# add route and function for /about page
# GET and POST requests are allowed
@app.route('/add', methods=['GET', 'POST'])
def add():
    # create an instance of AddTaskForm
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        # create a task object with title as provided in the form
        t = Task(title=form.title.data,
                 date=datetime.utcnow())
        # add the task to oour database
        db.session.add(t)
        db.session.commit()
        # redirect to index html page with new information
        return redirect(url_for('index'))
    # return about.html template and include the task form
    return render_template('add.html', form=form)