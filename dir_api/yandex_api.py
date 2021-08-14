from dir_api.__init__ import *

class YandexGeolocationApi:

    def __init__(self, geolocator_api_key:str="") -> None:
        self._geolocator_api_key = geolocator_api_key

    def search_by_address(self,address:str) -> str:
        """
        This method via Yandex Geolocation API find the geolocation of given address in JSON format
        :param address: <str> address entered by user
        :return:
        """

        request_str: str="https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s&format=json" %(self._geolocator_api_key,address) #temporary variable
        request:models.Response=get(request_str) #HTTP GET request for given geocode

        if (request.status_code==200):
            request_result:str=request.text
            return request_result

        elif (request.status_code==400): # bad request
            print("The request uses an invalid parameter or value. Additional information is provided in the error message.")

        elif (request.status_code==403): # forbidden
            print("	The request uses an invalid API key. Make sure you are using the correct API key")

    def get_geolocation(self,address:str) -> tuple:
        address_dict:dict=loads(address) #loads function return loads
        address_dict=address_dict["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        address_geolocation:tuple=tuple(address_dict.split(" "))
        return address_geolocation


if (__name__=="__main__"):
    yandex_obj : YandexGeolocationApi = YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
    result_str : str = yandex_obj.search_by_address("Ankara")
    yandex_obj.get_geolocation(result_str)
