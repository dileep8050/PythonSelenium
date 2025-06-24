import configparser
import os

class ConfigReader:
    def __init__(self, file_path=None):
        # Get the absolute path to the config.ini relative to this file
        base_path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(base_path, "..", "configurations", "config.ini")

        self.config = configparser.RawConfigParser()
        self.config.read(config_path)

    def get(self, key, section='DEFAULT'):
        return self.config.get(section, key, fallback=None)

