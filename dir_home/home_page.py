from dir_home.__init__ import *
from dir_api.yandex_api import YandexGeolocationApi
from dir_distance.distance import Distance
home_page = Blueprint('dir_home', __name__, template_folder='templates', static_folder='static')

@home_page.route('/',methods=["GET","POST"])
def home_page_function():
    try:
        if request.method=="GET":
            return render_template("home_page.html")

        elif request.method=="POST":
            #get address from home_page.html when POST reqeust executed
            given_address:str=request.form["address"]
            #create YandexGeolocationApi object with API KEY
            api_object=YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
            #get geolocation of given address with get_geolocation method
            geolocation: tuple=api_object.get_geolocation(api_object.search_by_address(given_address))
            distance_object=Distance()
            result_list:list=distance_object.find_nearest_point_mkad(geolocation)
            #logging to a file
            logging.basicConfig(filename="output.log", filemode="w", encoding="utf-8",level=logging.INFO)
            result="Origin-->"+str(result_list[0:2])+" Destination-->"+str(result_list[2:4])+" Distance(KM)-->"+str(result_list[4:])
            logging.info(str(result))
            return render_template("home_page.html")

    except TemplateNotFound:
        abort(404)
