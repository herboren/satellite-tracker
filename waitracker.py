from geopy.geocoders import Nominatim

class WhereAmITracker():

    # Return Float Location
    def ReturnLocation(position):
        try:
            geolocation = Nominatim(user_agent='sattracker.py')
            location = geolocation.geocode(position)
            return  [float(location.latitude),float(location.longitude)]
        except Exception as e:
            print(e)