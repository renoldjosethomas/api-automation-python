"""
DEV ACCOUNT: Dict for multiple users and its data for DEV Environment

return: dict for all users
"""

_API_BASEPATH = 'https://renold.free.beeceptor.com/'


data = {}
data['env'] = 'dev'

###### ENDPOINTS ######
data['API_BASEPATH'] = _API_BASEPATH

###### renauto1 ######
renauto1 = {}
renauto1['auth_id'] = 'xxxxxx'
renauto1['auth_token'] = 'yyyyyyy'

# PROFILE DATA
renauto1['profile'] = {}
renauto1['profile']['create'] = '149c3016-6c1a-41d8-8c2e-0b6bd1f570d2'
renauto1['profile']['get'] = '12acdc34-68b3-4465-9344-48cc5d2d6274'
renauto1['profile']['update'] = 'fa8ecff1-41fd-41d5-b9a2-8473553c54e6'
renauto1['profile']['delete'] = '3e57cbfa-0a29-4427-99d3-32d2cb6d0c7a'

# Add renauto1 to the data dictionary
data['renauto1'] = renauto1

###### renauto2 ######
renauto2 = {}
renauto2['auth_id'] = 'aaaaaaa'
renauto2['auth_token'] = 'bbbbbbb'

# PROFILE DATA
renauto2['profile'] = {}
renauto2['profile']['create'] = '5e627a15-5cb7-44ac-b279-55f7c69a6f58'
renauto2['profile']['get'] = '707ca587-52a4-44c9-b90e-697d9f56639c'
renauto2['profile']['update'] = '9b9e7485-bb83-4974-b4de-6723b3e1255f'
renauto2['profile']['delete'] = '3f45bbd2-6c2b-4b7d-bd6c-76a8d0a9712a'

# Add renauto2 to the data dictionary
data['renauto2'] = renauto2