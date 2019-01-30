from . import *

class REGIONS(db.Model):
    __tablename__ = 'REGIONS'
    REGION_ID = db.Column(db.Integer(), primary_key = True)
    REGION_NAME = db.Column(db.String(25))
