import json
import atexit
import os

from sys import platform
from datetime import datetime
from xmlrpc.client import DateTime

if 'win' in platform:
    CACHE_DIR = os.path.join(os.getenv('APPDATA'), 'shift_code_scraper')
else:
    CACHE_DIR = os.path.join(os.path.expanduser('~'), '.shift_code_scraper')
CACHE_FILE = os.path.join(CACHE_DIR, 'cache')

def _validate_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

class Cache:

    def __init__(self):
        _validate_cache_dir()
        atexit.register(self._dump_cache)
        self.cache = self._load_cache()

    def exists(self, key):
        return True if key in self.cache else False

    def add(self, key, expires):
        self.cache[key] = expires

    def _cleanup(self):
        pass

    def _load_cache(self):
        cache = {}
        try:
            with open(CACHE_FILE, 'r') as f:
                c = json.load(f)
                for k, v in c.items():
                    cache[k] = datetime.strptime(v, "%m/%d/%Y, %H:%M:%S")
            return cache
        except:
            return {}

    def _dump_cache(self):
        cache = {}

        for k, v in self.cache.items():
            cache[k] = v.strftime("%m/%d/%Y, %H:%M:%S")

        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f)

cache = Cache()
