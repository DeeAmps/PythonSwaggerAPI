from flask import Flask
from flask_restplus import Api, Resource
from .config import *
app = Flask(__name__)
app.config.from_object('config')

base_url = app.config.get("BASE_URL")
host = app.config.get("HOST")
port = app.config.get("PORT")
environment = app.config.get("ENV")
debug = app.config.get("DEBUG")
connectionStr = app.config.get("DB_CONNECTION")

api = Api(app,
          version=app.config.get("SAWGGER_API_VERSION"),
          title=app.config.get("SWAGGER_TITLE"),
          description=app.config.get("SWAGGER_DESCRIPTION"),
          doc="/api-docs",
          prefix="/api",
          contact="Daniel Bennin",
          contact_email="danyelamps.db@gmail.com")


#NameSpaces
employees = api.namespace('Employees', description="API endpoint for Oracle HR Database - Employees Table", path="/")
departments = api.namespace('Departments', description="API endpoint for Oracle HR Database - Departments Table", path="/")
jobs = api.namespace('Jobs', description="API endpoint for Oracle HR Database - Jobs Table", path="/")
locations = api.namespace('Locations', description="API endpoint for Oracle HR Database - Locations Table", path="/")
regions = api.namespace('Regions', description="API endpoint for Oracle HR Database - Regions Table", path="/")
countries = api.namespace('Countries', description="API endpoint for Oracle HR Database - Countries Table", path="/")
