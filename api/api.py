class YandexGeolocationApi:

    def __init__(self, geolocator_api_key=""):
        self._geolocator_api_key = geolocator_api_key



    def search_by_address(self,address):
        """
        This method via Yandex Geolocation API find the geolocation of given address in JSON format
        :param address: <str> address entered by user
        :return:
        """
        import requests,json
        request_str="https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s&format=json" %(self._geolocator_api_key,address)
        request=requests.get(request_str)
        if (request.status_code==200):
            #temporary code part
            with open("get_result.json","a") as file:
                json.dump(request.text,file)

        elif (request.status_code==400): # bad request
            print("The request uses an invalid parameter or value. Additional information is provided in the error message.")

        elif (request.status_code==403): # forbidden
            print("	The request uses an invalid API key. Make sure you are using the correct API key")

    def search_by_coordinates(self):
        pass

ya=YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
ya.search_by_address("***")


