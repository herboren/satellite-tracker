from threading import Timer

from geopy import distance
from colorama import *

# Initialize Timer
def PositionTracking():

    t = Timer(5.0, PositionTracking)
    t.start()

