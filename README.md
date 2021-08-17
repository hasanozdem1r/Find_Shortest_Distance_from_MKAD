
![Moscow_Ring_Road](https://mobacommunity.com/media/moxie/files/e/er/eri/erik-geis/384865_original.jpg)
# Find Nearest point in Moscow Ring Road 

In this project, we find the geolocation of the address entered by the user using the Yandex API.
Then, using geolocation, we determine the distance and point to the nearest point on the Moscow Ring Road
To learn more about Moscow Ring Road [МКАД](https://en.wikipedia.org/wiki/Moscow_Ring_Road)
## Installation

1. Install [git](https://git-scm.com/) to your system
2. Get a free API Key at [Yandex Developer's Dashboard](https://developer.tech.yandex.ru/)
3. Clone the repository from github
```bash
  git clone https://github.com/hasanozdem1r/Find_Shortest_Distance_from_MKAD
```

    

    
## API Reference

Get a free API Key at [Yandex Developer's Dashboard](https://developer.tech.yandex.ru/)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required** Your API key |
| `geocode` | `string` | **Required** address |
| `format` | `string` | **Optional** xml / JSON |

#### Basic HTTP GET request search by address

```http
  GET https://geocode-maps.yandex.ru/1.x/?apikey=api_key&geocode=given_address
```

#### Basic HTTP GET request search by coordinates

```http
  GET https://geocode-maps.yandex.ru/1.x/?apikey=Your API key&geocode=latitude,longitude
```

Further reading [Yandex Geocoder API](https://yandex.com/dev/maps/geocoder/doc/desc/concepts/about.html)
## Authors

- [Hasan Özdemir](https://www.github.com/hasanozdem1r)

## Contributing

Contributions are always welcome!

See [contributing.md](https://github.com/github/docs/blob/main/CONTRIBUTING.md) for ways to get started.

Please adhere to this project's `code of conduct`.

  
## License

[The Unlicense](https://choosealicense.com/licenses/unlicense/)

  
