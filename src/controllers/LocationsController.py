from src.models.Locations import LOCATIONS

def GetAllLocations():
    try:
        output = []
        result = LOCATIONS.query.all()
        for item in result:
            locObj = {}
            locObj['LOCATION_ID'] = item.LOCATION_ID
            locObj['STREET_ADDRESS'] = item.STREET_ADDRESS
            locObj['POSTAL_CODE'] = item.POSTAL_CODE
            locObj['CITY'] = item.CITY
            locObj['STATE_PROVINCE'] = item.STATE_PROVINCE
            locObj['COUNTRY_ID'] = item.COUNTRY_ID
            output.append(locObj)
        return output
    except Exception as e:
        return { "status": "An error occurred. Contact support."}

def GetSingleLocation(locationId):
    try:
        item = LOCATIONS.query.filter(LOCATIONS.LOCATION_ID == locationId).first()
        if item is None or item == {}:
            return {}
            locObj = {}
        locObj['LOCATION_ID'] = item.LOCATION_ID
        locObj['STREET_ADDRESS'] = item.STREET_ADDRESS
        locObj['POSTAL_CODE'] = item.POSTAL_CODE
        locObj['CITY'] = item.CITY
        locObj['STATE_PROVINCE'] = item.STATE_PROVINCE
        locObj['COUNTRY_ID'] = item.COUNTRY_ID
        return locObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}