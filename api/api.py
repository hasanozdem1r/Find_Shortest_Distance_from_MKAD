import requests

#api-key > your_api_key

#Basic search by address
request_address=requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=YOUR_API_KEY&geocode=Тверская+6")

#Basic search by coordinates
request_coordinates=requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=YOUR_API_KEY&geocode=37.611347,55.760241")

