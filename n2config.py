import configparser
import os, pathlib

class ConfigSatTracker():

    # Save sat tracker
    def svsttrkr(self):
        config = configparser.RawConfigParser()
        # Case sensitivity
        config.optionxform=str

        # Custom Category
        config['SAT-TRACKER'] = {
            'url': 'https://api.n2yo.com/rest/v1/satellite',
            'id': 0,
            'observer_lat': 0.0,
            'observer_lng': 0.0,
            'observer_alt': 0.0,
            'seconds': 0,
            'apiKey=': os.environ.get('n2yo_api')

        }

        config['SATELLITES'] = {
            
        }

        # Save Config
        with open('n2config.ini', 'w') as configFile:
            config.write(configFile )
