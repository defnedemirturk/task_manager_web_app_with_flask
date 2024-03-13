
# we will keep the routes and functionalities here separately
# to know what is used as "app" and "render_template" 
# we will import them from app.py module
from app import app, db
from flask import render_template
from flask import redirect, url_for
# import libraries to display alert messages on page
from flask import flash, get_flashed_messages

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
        flash('Task added to the Database.')
        # redirect to index html page with new information
        return redirect(url_for('index'))
    # return about.html template and include the task form
    return render_template('add.html', form=form)

# editing functionality for a specified task (by its number)
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated!')
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('edit.html',
                               form=form,
                               task_id=task_id)
    return redirect(url_for('index'))

# delete functionality for a specified task (by its number)
@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been deleted!')
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('delete.html',
                               form=form,
                               task_id=task_id,
                               title=task.title)
    return redirect(url_for('index'))