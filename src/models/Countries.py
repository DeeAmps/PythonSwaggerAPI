from . import *

class COUNTRIES(db.Model):
    __tablename__ = 'COUNTRIES'
    COUNTRY_ID = db.Column(db.String(2) ,primary_key = True)
    COUNTRY_NAME = db.Column(db.String(30))
    REGION_ID = db.Column(db.Integer)
