from . import *

class JOBS(db.Model):
    __tablename__ = 'JOBS'
    JOB_ID = db.Column(db.Integer, primary_key = True)
    JOB_TITLE = db.Column(db.String(35))
    MIN_SALARY = db.Column(db.Integer)
    MAX_SALARY = db.Column(db.Integer)
