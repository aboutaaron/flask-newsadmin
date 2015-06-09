from app import db

# we have to import the models so that sqlalchemy can detect them and create the db
# how else would it know what to create ?
from app.admin.models import *

# creates the database
db.create_all()
