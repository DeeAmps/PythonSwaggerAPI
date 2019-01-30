from src.models.Jobs import JOBS

def GetAllJobs():
    try:
        output = []
        result = JOBS.query.all()
        for item in result:
            jobObj = {}
            jobObj['JOB_ID'] = item.JOB_ID
            jobObj['JOB_TITLE'] = item.JOB_TITLE
            jobObj['MIN_SALARY'] = item.MIN_SALARY
            jobObj['MAX_SALARY'] = item.MAX_SALARY
            output.append(jobObj)
        return output
    except Exception as e:
        return { "status": "An error occurred. Contact support."}

def GetSingleJob(jobId):
    try:
        item = JOBS.query.filter(JOBS.JOB_ID == jobId).first()
        if item is None or item == {}:
            return {}
            jobObj = {}
        jobObj['JOB_ID'] = item.JOB_ID
        jobObj['JOB_TITLE'] = item.JOB_TITLE
        jobObj['MIN_SALARY'] = item.MIN_SALARY
        jobObj['MAX_SALARY'] = item.MAX_SALARY
        return jobObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}