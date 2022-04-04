from discord import Webhook, RequestsWebhookAdapter, Embed

from . import logger
from .config import config

WEBHOOK = Webhook.from_url(config['MAIN']['discord_webhook'], adapter=RequestsWebhookAdapter())

def send_discord_alert(shift_keys):
    for shift_key in shift_keys:
        title = f'{shift_key.game} - {shift_key.reward} (exp. {shift_key.expires})'
        description = f'{shift_key.key}\n\n[redeem](https://shift.gearboxsoftware.com/rewards)'
        embed = Embed(title=title, description=description)

        logger.info(f'Sending discord alert\n{title}\n{description}')
        WEBHOOK.send('', embed=embed)
