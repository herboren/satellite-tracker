import configparser
from pathlib import Path
from threading import Timer
from geopy import distance
from colorama import *
from n2config import ConfigSatTracker

# Create config file
if not Path('n2config.ini').is_file():
    ConfigSatTracker.svsttrkr()

def ConfigUrl():
    # Create config read object, then open ini
    conf_st = configparser.ConfigParser()
    conf_st.read('n2config.ini')

    for category in conf_st.sections():
        # Assign parameters if present
        if category == 'SAT-TRACKER':
            for key, value in conf_st.sections(category):
                if value != 0


def GetJsonRequest():


# Initialize Timer
def PositionTracking():
    
    # Inquiry every 20sec
    t = Timer(20.0, PositionTracking)
    t.start()

