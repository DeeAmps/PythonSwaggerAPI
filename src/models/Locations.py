from . import *

class LOCATIONS(db.Model):
    __tablename__ = 'LOCATIONS'
    LOCATION_ID = db.Column(db.Integer(), primary_key = True)
    STREET_ADDRESS = db.Column(db.String(40))
    POSTAL_CODE = db.Column(db.String(12))
    CITY = db.Column(db.String(30))
    STATE_PROVINCE = db.Column(db.String(25))
    COUNTRY_ID = db.Column(db.String(2))
