
#* #** CSRF settings
from dev_core.settings.settings import *

if DEBUG:
    CSRF_COOKIE_DOMAIN = '*'  #*The domain to be used when setting the CSRF cookie. If set . before the domain name, then it also allow for subdomain.
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_NAME = '__Secure-csrftoken'
    CSRF_COOKIE_SAMESITE = 'Strict'
    CSRF_COOKIE_SECURE = True  #* browser trigger the cookie as safe, and only be send by secure connection.
    CSRF_USE_SESSIONS = True