from dotenv import load_dotenv
from dev_core.settings.settings import BASE_DIR
import os
from dev_core.types.export import *

load_dotenv(BASE_DIR / '.env')

KEY_TYPE = Literal['GOOGLE_ID', 'GOOGLE_SECRET', 'SECRET_KEY', 'DEBUG', 'API_ROUTE', 'MY_EMAIL', 'MY_EMAIL_PASSWORD', 'HOST_BE_LOCAL', 'HOST_BE_PRODUCTION']

