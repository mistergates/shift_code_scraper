import json
import atexit

from datetime import datetime

from . import CACHE_FILE, logger


class Cache:

    def __init__(self):
        atexit.register(self._dump_cache)
        self.cache = self._load_cache()

    def exists(self, key):
        return True if key in self.cache else False

    def add(self, key, expires):
        logger.info(f'Adding {key} to cache')
        self.cache[key] = expires
        self._dump_cache()

    def _cleanup(self):
        pass

    def _load_cache(self):
        cache = {}
        try:
            with open(CACHE_FILE, 'r') as f:
                c = json.load(f)
            for k, v in c.items():
                cache[k] = datetime.strptime(v, "%m/%d/%Y, %H:%M:%S")
        except:
            pass
        logger.info(f'Loading cache {cache}')
        return cache

    def _dump_cache(self):
        if not self.cache:
            return

        cache = {}

        for k, v in self.cache.items():
            cache[k] = v.strftime("%m/%d/%Y, %H:%M:%S")

        logger.info(f'Writing cache {json.dumps(cache, indent=4)}')
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f)

cache = Cache()
