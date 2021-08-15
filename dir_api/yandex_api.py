from dir_api.__init__ import *

class YandexGeolocationApi:

    def __init__(self, geolocator_api_key:str="") -> None:
        """
        __init__ is a  constructor is a special member function of a class that is executed whenever we create new objects of that class
        :param geolocator_api_key: <str>Yandex.Maps API Geocoder API key used for HTTP request
        """
        self._geolocator_api_key = geolocator_api_key

    def search_by_address(self,address:str) -> str:
        """
        This method via Yandex Geolocation API get the information of given address in JSON format
        :param address: <str> address entered by user
        :return: request_result <str> :information for given address
        """


        # HTTP error handling [200, 400, 403, 500, 503] First 3 items as informed in official document can be raised by API
        # but also 500 and 503 is common mistakes by user internet connection and server status therefore I have added.
        try:
            # Preparing HTTP request string by API_KEY and given address
            request_str: str="https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s&format=json" %(self._geolocator_api_key,address) #temporary variable
            # HTTP GET request for given address
            request_response:models.Response=get(request_str)

            # The request has succeeded.
            if (request_response.status_code==200): # HTTP 200 --> SUCCESSFUL
                request_result:str=request_response.text
                return request_result

        # The server could not understand the request due to invalid syntax. The client SHOULD NOT repeat the request without modifications.
        except BadRequest as error: # HTTP 400 --> Bad Request
            error_msg: str = "Error: {}".format(error)
            return error_msg

        # The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource.
        # Unlike 401, the client's identity is known to the server.
        except Forbidden as error: # HTTP 403 --> Forbidden (wrong API Key)
            error_msg: str = "Error: {}".format(error)
            return error_msg

        # The server has encountered a situation it doesn't know how to handle.
        except exceptions.ConnectionError as error: # Internal Server Error 500
            error_msg:str="Error: {}".format(error)
            return error_msg

        # Any other error which is not so common
        except exceptions.RequestException as error:
            error_msg:str="Error: {}".format(error)
            return error_msg

    def get_geolocation(self,address:str) -> tuple:
        """
        This method return geolocation from given JSON file about given address (latitude,longitude)
        :param address: <str> Given address information in JSON data structure
        :return: <tuple> address_geolocation is a latitude and longitude information of address
        """

        # loads function used to parse a valid JSON string and convert it into python dictionary
        address_dict:dict=loads(address)
        # filter result (dict type) to receive geolocation information
        address_dict=address_dict["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        # convert result to tuple
        address_geolocation:tuple=tuple(address_dict.split(" "))
        # result in opposite order <longitude, latitude) therefore we convert this to correct order <latitude, longitude>
        # also api return keep information as string therefore we return it to float type  --> (float(latitude), float(langitude))
        address_geolocation=(float(address_geolocation[1]),float(address_geolocation[0]))
        # we received for given address geolocation from http_response and return
        return address_geolocation

# here can be used while you test your code.
# if you call this class from another file this part will not be executed
if (__name__=="__main__"):
    yandex_obj : YandexGeolocationApi = YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
    result_str : str = yandex_obj.search_by_address("Ankara")
    #a=yandex_obj.get_geolocation(result_str)
    #print(type(result_str),result_str)
