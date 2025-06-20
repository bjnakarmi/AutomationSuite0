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
