from . import *

class EMPLOYEES(db.Model):
    __tablename__ = 'EMPLOYEES'
    EMPLOYEE_ID = db.Column(db.Integer, primary_key = True)
    FIRST_NAME = db.Column(db.String(20))
    LAST_NAME = db.Column(db.String(25))
    EMAIL = db.Column(db.String(25))
    PHONE_NUMBER = db.Column(db.String(25))
    HIRE_DATE = db.Column(db.Date)
    JOB_ID = db.Column(db.String(10))
    SALARY = db.Column(db.String(25))
    COMMISSION_PCT = db.Column(db.String(10))
    MANAGER_ID = db.Column(db.Integer)
    DEPARTMENT_ID = db.Column(db.Integer)