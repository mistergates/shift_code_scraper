import feedparser

from datetime import datetime, timedelta

from cache import cache
from config import config


URL = 'https://shift.orcicorn.com/index.xml'


class _ShiftCode:

    def __init__(self, game, published, expires, platform, reward, key):
        self.game = game
        self.published = self._convert_published(published)
        self.expires = self._convert_expires(expires)
        self.platform = platform
        self.reward = reward
        self.key = key

    def _convert_expires(self, date):
        if date == 'Unknown':
            return datetime.now() + timedelta(days=30)
        return datetime.strptime(date, '%d %b %Y %H:%M:%S')

    def _convert_published(self, date):
        if date == 'Unknown':
            return datetime.now()
        return datetime.strptime(date, '%a %d %b %Y %H:%M:%S')


def parse():
    codes = []
    feed = feedparser.parse(URL)
    game_filter = config.get('MAIN', 'game')

    for entry in feed['entries']:
        code = _ShiftCode(
            entry['shift_game'],
            entry['published'].split('-')[0].strip().replace(',', ''),
            entry['shift_expires'].split('-')[0].strip(),
            entry['shift_platform'],
            entry['shift_reward'],
            entry['shift_code']
        )

        if cache.exists(code.key):
            continue

        if game_filter and code.game != game_filter:
            continue

        if datetime.now() > code.expires:
            continue

        codes.append(code)
        cache.add(code.key, code.expires)

    return codes
