import os
import sys

from sys import platform
from loguru import logger


if 'win' in platform:
    APP_DIR = os.path.join(os.getenv('APPDATA'), 'shift_code_scraper')
else:
    APP_DIR = os.path.join(os.path.expanduser('~'), '.shift_code_scraper')


if not os.path.exists(APP_DIR):
    os.makedirs(APP_DIR)


CACHE_FILE = os.path.join(APP_DIR, 'cache')

logger.remove()
logger.add(sys.stderr, level='INFO')
logger.add(os.path.join(APP_DIR, 'app.log'), rotation='5 MB', level='INFO')
