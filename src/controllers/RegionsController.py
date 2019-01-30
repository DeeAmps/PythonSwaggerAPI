from src.models.Regions import REGIONS


def GetAllRegions():
    try:
        output = []
        result = REGIONS.query.all()
        for item in result:
            regObj = {}
            regObj['REGION_ID'] = item.REGION_ID
            regObj['REGION_NAME'] = item.REGION_NAME
            output.append(regObj)
        return output
    except Exception as e:
        return { "status": "An error occurred. Contact support."}

def GetSingleRegion(regionId):
    try:
        item = REGIONS.query.filter(REGIONS.REGION_ID == regionId).first()
        if item is None or item == {}:
            return {}
        regObj = {}
        regObj['REGION_ID'] = item.REGION_ID
        regObj['REGION_NAME'] = item.REGION_NAME
        return regObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}