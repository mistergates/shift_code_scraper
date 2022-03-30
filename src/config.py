import os

from configparser import ConfigParser

CONFIG_FILE = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'config.ini')

config = ConfigParser()
config.read(CONFIG_FILE)
