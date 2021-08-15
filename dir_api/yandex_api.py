from dir_api.__init__ import *

class YandexGeolocationApi:

    def __init__(self, geolocator_api_key:str="") -> None:
        self._geolocator_api_key = geolocator_api_key

    def search_by_address(self,address:str) -> str:
        """
        This method via Yandex Geolocation API get the information of given address in JSON format
        :param address: <str> address entered by user
        :return: request_result <str> :information for given address
        """

        request_str: str="https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s&format=json" %(self._geolocator_api_key,address) #temporary variable
        request_response:models.Response=get(request_str) #HTTP GET request for given geocode

        """
        HTTP error handling [200, 400, 403, 500, 503] First 3 items as informed in official document can be raised by API
        but also 500 and 503 is common mistakes by user internet connection and server status therefore I have added.
        """
        # The request has succeeded.
        if (request_response.status_code==200): # successful request
            request_result:str=request_response.text
            return request_result

        #The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.
        elif (request_response.status_code==400): # bad request
            abort(400,"The request uses an invalid parameter or value.")

        # The server understood the request, but is refusing to fulfill it. Authorization will not help and the request SHOULD NOT be repeated.
        elif (request_response.status_code==403): # forbidden
            abort(403,"	The request uses an invalid API key. Make sure you are using the correct API key")

        # The server understood the request, but is refusing to fulfill it. Authorization will not help and the request SHOULD NOT be repeated.
        elif (request_response.status_code==500): # Internal Server Error
            abort(500, "The server encountered an unexpected condition which prevented it from fulfilling the request.")

        # The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.
        elif (request_response.status_code==503): # Service Unavailable
            abort(503,"The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. ")

    def get_geolocation(self,address:str) -> tuple:
        """
        This method return geolocation from given JSON file about given address (latitude,longitude)
        :param address: <str> Given address information in JSON data structure
        :return: <tuple> address_geolocation is a latitude and longitude information of address
        """
        # loads function used to parse a valid JSON string and convert it into python dictionary
        address_dict:dict=loads(address)
        # filter result to get geolocation information
        address_dict=address_dict["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        # convert result to tuple
        address_geolocation:tuple=tuple(address_dict.split(" "))
        # result in opposite order <longitude, latitude) we convert this to correct order <latitude, longitude>
        address_geolocation=(float(address_geolocation[1]),float(address_geolocation[0]))
        # return address geolocation example -> Moscow ('55.75322', '37.622513')
        return address_geolocation

if (__name__=="__main__"):
    yandex_obj : YandexGeolocationApi = YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
    result_str : str = yandex_obj.search_by_address("Istanbul")
    a=yandex_obj.get_geolocation(result_str)
    print(type(a),a)
