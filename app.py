# @author : Defne Demirtuerk
# Python Flask web application


# app.py module is the entry point to our web application
# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create an instance (application) of the Flask class
app = Flask(__name__)

# set up configuration keys 
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# create our database instance
# this instance will use models.py module for data model 
db = SQLAlchemy(app)

# after the app has been instantiated 
# we should import all from routes.py module
# so that the app instance can be used in route functions
from routes import *


'''
def index_as_txt():
    #returns text value for the GET request at /index page and / page
    return "Hello World!"
'''


if __name__ == '__main__':
    app.run(debug=True)