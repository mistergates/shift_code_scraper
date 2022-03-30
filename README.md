# SHiFT Code Scraper
Scrape shift codes for a specified game and send alerts for new codes to a Discord channel via a webhook

## Configuration
* Create a Python 3.9+ virtual environment
* Install requirements via `pip install -r requirements.txt`
* Update `config.ini`
    * Add discord webhook URL
    * Change game (Leave blank to not filter by game)

## Run
* Start the scraper in your virtual environment (will run until terminated) via `python shift_code_scraper.py`