"""
DEV ACCOUNT: Dict for multiple users and its data for DEV Environment

return: dict for all users
"""

_API_BASEPATH = 'https://renold.free.beeceptor.com/'

data = {}
data['env'] = 'dev'

# renauto1:
data['renauto1'] = {
    'auth_id': 'xxxxxx',
    'auth_token': 'yyyyyyy',
    'profile_uuid': '930469e9-8f15-4843-80a8-d6de887bc493',
}

# renauto2:
data['renauto2'] = {
    'auth_id': 'aaaaaaa',
    'auth_token': 'bbbbbbb',
    'profile_uuid': '920469e9-8f15-4843-80a8-d6de887bc493',
}

data['API_BASEPATH'] = _API_BASEPATH