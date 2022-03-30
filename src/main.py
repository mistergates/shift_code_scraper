import time

from .shift_code_parser import parse
from .config import config
from .alerts import send_discord_alert

def main():
    while True:
        try:
            codes = parse()
            if codes:
                send_discord_alert(codes)
        except Exception as e:
            print(e)

        time.sleep(config.getint('MAIN', 'scrape_interval_seconds'))


if __name__ == '__main__':
    main()
