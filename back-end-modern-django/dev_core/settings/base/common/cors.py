
from dev_core.settings.settings import *
CORS_ALLOW_ALL_ORIGINS = True  # not allow access from all request.
CORS_ALLOW_CREDENTIALS = False  # not allow access cookie
CORS_ALLOW_PRIVATE_NETWORK = True  # not public Ip address

if DEBUG:
    CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
else:
    CORS_ORIGIN_WHITELIST = [FRONT_END_URL,]
# print(CORS_ORIGIN_WHITELIST)
# CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]