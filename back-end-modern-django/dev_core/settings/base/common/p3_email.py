
#* Email settings for Django
from dev_core.settings.settings import *


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = MY_EMAIL
EMAIL_HOST_PASSWORD = MY_EMAIL_PASSWORD