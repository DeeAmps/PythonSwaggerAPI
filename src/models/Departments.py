from . import *

class DEPARTMENTS(db.Model):
    __tablename__ = 'DEPARTMENTS'
    DEPARTMENT_ID = db.Column(db.Integer, primary_key = True)
    DEPARTMENT_NAME = db.Column(db.String(30))
    MANAGER_ID = db.Column(db.Integer)
    LOCATION_ID = db.Column(db.Integer)
