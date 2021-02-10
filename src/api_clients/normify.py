''' helper functions for api returns '''

import json

def normify(input_dict):
    ''' removes ordered dicts '''
    return json.loads(json.dumps(input_dict))