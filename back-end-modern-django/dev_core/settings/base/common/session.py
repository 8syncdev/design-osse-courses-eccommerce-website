
#* #** Security settings for the CSRF middleware
from dev_core.settings.settings import *

if DEBUG:
    SESSION_COOKIE_DOMAIN = '*'  #* The domain to use for session cookies. 
    SESSION_COOKIE_HTTPONLY = True  #* session cookies can only be access by https request.
    SESSION_COOKIE_NAME = '__Secure-sessionid'
    SESSION_COOKIE_SAMESITE = 'Strict'
    SESSION_COOKIE_SECURE = True  #* browser trigger the session cookie as safe, and only be send by secure connection.
    SESSION_SAVE_EVERY_REQUEST = True