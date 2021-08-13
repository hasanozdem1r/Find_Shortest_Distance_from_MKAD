class Distance:

    def __init__(self):
        pass

    def find_distance_haversine(self, origin:tuple, destination:tuple):
        """
        find_distance_haversine function use Haversine formula to determine distance between 2 geolocation.
        The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.
        :param origin: <tuple:(latitude,longitude)> starting point.
        :param destination: <tuple:(latitude,longitude)> arrival point.
        :return: distance <float> distance between origin and destination as KM
        """

        from math import radians, sin, cos, atan2, sqrt
        RADIUS = 6371  # A straight line from the centre to the circumference of a circle or sphere.
        lat1, lon1 = origin
        lat2, lon2 = destination

        distance_lat = radians(lat2 - lat1)
        distance_lon = radians(lon2 - lon1)
        a = sin(distance_lat / 2) ** 2 + cos(radians(lat1)) \
            * cos(radians(lat2)) * sin(distance_lon / 2) ** 2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = RADIUS * c  # Great Circle Arc Length(distance)

        return distance