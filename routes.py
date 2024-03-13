
# we will keep the routes and functionalities here separately
# to know what is used as "app" and "render_template" 
# we will import them from app.py module
from app import app
from flask import render_template

# import our forms
import forms


# we will define routes to make the app capable of hosting different url sites
# we can return text/html and other values such as JSON as return value of a route
# we will use decorators to tell our server that we want to run the function 
# defined below to be run at the specified url path
@app.route('/')          # we can use multiple routes with the same function
@app.route('/index')     # the index folder
def index():
    #returns html value forthe GET request at /index page and / page
    #return '<h1>Hello</h1> World!'
    # return the html content from an html file with specific variable values
    return render_template('index.html')


# add route and function for /about page
@app.route('/about')
def about():
    # create an instance of AddTaskForm
    form = forms.AddTaskForm()
    # return about.html template and include the task form
    return render_template('about.html', form=form)