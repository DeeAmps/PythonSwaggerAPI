from src.models.Employees import EMPLOYEES


def GetAllEmployees():
    try:
        output = []
        result = EMPLOYEES.query.all()
        for item in result:
            empObj = {}
            empObj['EMPLOYEE_ID'] = item.EMPLOYEE_ID
            empObj['FIRST_NAME'] = item.FIRST_NAME
            empObj['LAST_NAME'] = item.LAST_NAME
            empObj['EMAIL'] = item.EMAIL
            empObj['PHONE_NUMBER'] = item.PHONE_NUMBER
            empObj['HIRE_DATE'] = item.HIRE_DATE.strftime('%x')
            empObj['JOB_ID'] = item.JOB_ID
            empObj['SALARY'] = str(item.SALARY)
            empObj['COMMISSION_PCT'] = str(item.COMMISSION_PCT)
            empObj['MANAGER_ID'] = item.MANAGER_ID
            empObj['DEPARTMENT_ID'] = item.DEPARTMENT_ID
            output.append(empObj)
        return output
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}

def GetSingleEmployees(employeeId):
    try:
        item = EMPLOYEES.query.filter(EMPLOYEES.EMPLOYEE_ID == employeeId).first()
        if item is None or item == {}:
            return {}
        empObj = {}
        empObj['EMPLOYEE_ID'] = item.EMPLOYEE_ID
        empObj['FIRST_NAME'] = item.FIRST_NAME
        empObj['LAST_NAME'] = item.LAST_NAME
        empObj['EMAIL'] = item.EMAIL
        empObj['PHONE_NUMBER'] = item.PHONE_NUMBER
        empObj['HIRE_DATE'] = item.HIRE_DATE.strftime('%x')
        empObj['JOB_ID'] = item.JOB_ID
        empObj['SALARY'] = str(item.SALARY)
        empObj['COMMISSION_PCT'] = str(item.COMMISSION_PCT)
        empObj['MANAGER_ID'] = item.MANAGER_ID
        empObj['DEPARTMENT_ID'] = item.DEPARTMENT_ID
        return empObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}