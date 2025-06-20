import requests
from utils.config import CONFIG

def get_all_trainings(headers):
    endpoint = 'api/globalSetting/trainingVideo/getAllByPanel'
    params = {
        'page' : 1,
        'offset' : 0,
        'trainingVideoCategoryId' : 23
    }
    response = requests.get(CONFIG['api_base'] + endpoint, params=params, headers=headers )
    return response


def get_all_suppliers(header):
    endpoint = '/api/company/getAll'
    params = {
        'countryId' : 5,
        'page' : 1,
        'isActive' : True,
        'limit' : 10,
        'offset' : 0

    }
    response = requests.get(url = CONFIG['api_base'] + endpoint,params= params, headers=header)
    return response