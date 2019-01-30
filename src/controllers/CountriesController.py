from src.models.Countries import COUNTRIES

def GetAllCountries():
    try:
        output = []
        result = COUNTRIES.query.all()
        for item in result:
            countObj = {}
            countObj['COUNTRY_ID'] = item.COUNTRY_ID
            countObj['COUNTRY_NAME'] = item.COUNTRY_NAME
            countObj['REGION_ID'] = item.REGION_ID
            output.append(countObj)
        return output
    except Exception as e:
        return { "status": "An error occurred. Contact support."}

def GetSingleCountry(countryId):
    try:
        item = COUNTRIES.query.filter(COUNTRIES.COUNTRY_ID == countryId).first()
        if item is None or item == {}:
            return {}
        countObj = {}
        countObj['COUNTRY_ID'] = item.COUNTRY_ID
        countObj['COUNTRY_NAME'] = item.COUNTRY_NAME
        countObj['REGION_ID'] = item.REGION_ID
        return countObj
    except Exception as e:
        print(str(e))
        return { "status": "An error occurred. Contact support."}