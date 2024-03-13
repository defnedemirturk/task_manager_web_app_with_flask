# @author : Defne Demirtuerk
# This module includes the necessary python code for CLI to create a database instance

from app import db

db.create_all()

from models import Task
from datetime import datetime


t = Task(title="xyz", date=datetime.utcnow())
print(t)
db.session.add(t)
db.session.commit()

t_2 = Task(title="abc", date=datetime.utcnow())
print(t_2)
db.session.add(t_2)
db.session.commit()

tasks = Task.query.all()
print(tasks)