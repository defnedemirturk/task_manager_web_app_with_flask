# @author : Defne Demirtuerk

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Add Task form
class AddTaskForm(FlaskForm):
    # we can specify many validators as a list
    # here we only use DataRequired to make sure 
    # the user does not leave the field empty
    title = StringField('Title', validators=[DataRequired()])
    # we also create a submit button
    submit = SubmitField('Submit')


class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')