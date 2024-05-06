'''
This file is used to export all the types that are used in the dev_core package.
'''
from dev_core.types.base_type import *

HTTP_METHOD_NAME_TYPE = Literal['get','post','put','delete','patch','head','options','trace']


KEY_TYPE = Literal['GOOGLE_ID', 'GOOGLE_SECRET', 'SECRET_KEY', 'DEBUG', 'API_ROUTE', 'MY_EMAIL', 'MY_EMAIL_PASSWORD', 'HOST_BE_LOCAL', 'HOST_BE_PRODUCTION']