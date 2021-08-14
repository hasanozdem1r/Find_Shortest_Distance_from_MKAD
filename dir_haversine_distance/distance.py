from dir_haversine_distance._init__ import *

class Distance:

    def __init__(self) -> None:
        pass

    def find_distance_haversine(self, origin:tuple, destination:tuple) -> float:
        """
        find_distance_haversine function use Haversine formula to determine distance between 2 geolocation.
        The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.
        :param origin: <tuple:(latitude,longitude)> starting point.
        :param destination: <tuple:(latitude,longitude)> arrival point.
        :return: distance <float> distance between origin and destination as KM
        """
        # Earth radius in kilometers. A straight line from the centre to the circumference of a circle or sphere.
        RADIUS : int = 6372.8

        #latitude and longitude values for given point (origin) and shortest point(destinatio)
        lat_origin : float=origin[0]
        lon_origin : float=origin[1]
        lat_destination:float=destination[0]
        lon_destination :float=destination[1]

        #latitude,longitude distance between two addresses
        distance_lat :float = radians(lat_destination - lat_origin)
        distance_lon :float= radians(lon_destination - lon_origin)
        #to be done
        a = sin(distance_lat / 2) ** 2 + cos(radians(lat_origin)) \
            * cos(radians(lat_destination)) * sin(distance_lon / 2) ** 2
        #to be done
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        #distance between origin and destination as kilometers
        distance = RADIUS * c  # Great Circle Arc Length(distance)
        return distance

if (__name__=="__main__"):
    distance_obj=Distance()
    distance_obj.find_distance_haversine((41.034768859043716, 28.954126450754607),(55.77075241893481, 37.56248403199888)) #Istanbul -> 41.034768859043716, 28.954126450754607 Moscow -> 55.77075241893481, 37.56248403199888