from src import *
from src.controllers import EmployeesController, \
    RegionsController, CountriesController, DepartmentsController, JobsController, \
    LocationsController

from flask_api import status

parser = api.parser()

@locations.route('/locations/getSingleLocation/<int:id>', endpoint='getSingleLocation')
class getSingleLocation(Resource):
    @locations.doc('Get Single Job')
    @locations.doc(responses={'200' : 'Success', '404' : 'Location not found'})
    @locations.doc(params={'id': 'Job ID'})
    @locations.doc(description="Get a single Location from Oracle HR Database")
    def get(self, id):
        res = LocationsController.GetSingleLocation(id)
        if res == {}:
            res = { "status": "Location not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK

@locations.route('/locations/getAllLocations', endpoint='getAllLocations')
class getAllLocations(Resource):
    @locations.doc('Get All Locations')
    @locations.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @locations.doc(description="Get all Locations from Oracle HR Database")
    def get(self):
        res = LocationsController.GetAllLocations()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK


@jobs.route('/jobs/getSingleJob/<int:id>', endpoint='getSingleJob')
class getSingleJob(Resource):
    @jobs.doc('Get Single Job')
    @jobs.doc(responses={'200' : 'Success', '404' : 'Job not found'})
    @jobs.doc(params={'id': 'Job ID'})
    @jobs.doc(description="Get a single Job from Oracle HR Database")
    def get(self, id):
        res = JobsController.GetSingleJob(id)
        if res == {}:
            res = { "status": "Job not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK

@jobs.route('/jobs/getAllJobs', endpoint='getAllJobs')
class getAllJobs(Resource):
    @jobs.doc('Get All Jobs')
    @jobs.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @jobs.doc(description="Get all Jobs from Oracle HR Database")
    def get(self):
        res = JobsController.GetAllJobs()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK

@departments.route('/departments/getSingleDepartment/<int:id>', endpoint='getSingleDepartment')
class getSingleDepartment(Resource):
    @departments.doc('Get Single Employee')
    @departments.doc(responses={'200' : 'Success', '404' : 'Department not found'})
    @departments.doc(params={'id': 'Department ID'})
    @departments.doc(description="Get a single Department from Oracle HR Database")
    def get(self, id):
        res = DepartmentsController.GetSingleDepartment(id)
        if res == {}:
            res = { "status": "Department not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK

@departments.route('/departments/getAllDepartments', endpoint='getAllDepartments')
class getAllDepartments(Resource):
    @departments.doc('Get All Departments')
    @departments.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @departments.doc(description="Get all Departments from Oracle HR Database")
    def get(self):
        res = DepartmentsController.GetAllDepartments()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK

@countries.route('/countries/getSingleCountry/<int:id>', endpoint='getSingleCountry')
class getSingleCountry(Resource):
    @countries.doc('Get Single Employee')
    @countries.doc(responses={'200' : 'Success', '404' : 'Country not found'})
    @countries.doc(params={'id': 'Country ID'})
    @countries.doc(description="Get a single Country from Oracle HR Database")
    def get(self, id):
        res = CountriesController.GetSingleCountry(id)
        if res == {}:
            res = { "status": "Country not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK

@countries.route('/regions/getAllCountries', endpoint='getAllCountries')
class getAllCountries(Resource):
    @countries.doc('Get All Countries')
    @countries.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @countries.doc(description="Get all Countries from Oracle HR Database")
    def get(self):
        res = CountriesController.GetAllCountries()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK

@regions.route('/regions/getSingleRegion/<int:id>', endpoint='getSingleRegion')
class getSingleRegion(Resource):
    @regions.doc('Get Single Employee')
    @regions.doc(responses={'200' : 'Success', '404' : 'Region not found'})
    @regions.doc(params={'id': 'Region ID'})
    @regions.doc(description="Get a single Region from Oracle HR Database")
    def get(self, id):
        res = RegionsController.GetSingleRegion(id)
        if res == {}:
            res = { "status": "Region not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK

@regions.route('/regions/getAllRegions', endpoint='getAllRegions')
class getAllRegions(Resource):
    @regions.doc('Get All Regions')
    @regions.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @regions.doc(description="Get all Regions from Oracle HR Database")
    def get(self):
        res = RegionsController.GetAllRegions()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK

@employees.route('/employees/getAllEmployees', endpoint='getAllEmployees')
class getAllEmployees(Resource):
    @employees.doc('Get All Employees')
    @employees.doc(responses={'500' : 'Internal Server Error', '200' : 'Success'})
    @employees.doc(description="Get all Employees from Oracle HR Database")
    def get(self):
        res = EmployeesController.GetAllEmployees()
        if not isinstance(res, list):
            return res, status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            return res, status.HTTP_200_OK

@employees.route('/employees/getSingleEmployee/<int:id>', endpoint='getSingleEmployee')
class getSingleEmployees(Resource):
    @employees.doc('Get Single Employee')
    @employees.doc(responses={'200' : 'Success', '404' : 'Employee not found'})
    @employees.doc(params={'id': 'Employee ID'})
    @employees.doc(description="Get a single Employee from Oracle HR Database")
    def get(self, id):
        res = EmployeesController.GetSingleEmployees(id)
        if res == {}:
            res = { "status": "Employee not found." }
            return res, status.HTTP_404_NOT_FOUND
        else:
            return res, status.HTTP_200_OK


if __name__ == '__main__':
    app.run(debug=debug, threaded=True,host=host, port=port)
