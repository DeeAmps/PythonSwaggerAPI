from src.models.Departments import DEPARTMENTS

def GetAllDepartments():
    try:
        output = []
        result = DEPARTMENTS.query.all()
        for item in result:
            depObj = {}
            depObj['DEPARTMENT_ID'] = item.DEPARTMENT_ID
            depObj['DEPARTMENT_NAME'] = item.DEPARTMENT_NAME
            depObj['MANAGER_ID'] = item.MANAGER_ID
            depObj['LOCATION_ID'] = item.LOCATION_ID
            return depObj
            output.append(depObj)
        return output
    except Exception as e:
        return { "status": "An error occurred. Contact support."}

def GetSingleDepartment(departmentId):
    try:
        item = DEPARTMENTS.query.filter(DEPARTMENTS.DEPARTMENT_ID == departmentId).first()
        if item is None or item == {}:
            return {}
        depObj = {}
        depObj['DEPARTMENT_ID'] = item.DEPARTMENT_ID
        depObj['DEPARTMENT_NAME'] = item.DEPARTMENT_NAME
        depObj['MANAGER_ID'] = item.MANAGER_ID
        depObj['LOCATION_ID'] = item.LOCATION_ID
        return depObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}