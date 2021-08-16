from dir_home.__init__ import *


home_page = Blueprint('dir_home', __name__, template_folder='templates', static_folder='static')

@home_page.route('/',methods=["GET","POST"])
def home_page_function() -> str:
    """
    home_home_page_function regarding to HTTP request will return html file or log shortest distance
    :return: <str> logging or html
    """

    #this try except block handle with HtmlNotFoundError
    try:
        if request.method=="GET":
            return render_template("home_page.html")

        elif request.method=="POST":
            #get address from home_page.html when POST reqeust executed
            given_address:str=str(request.form["address"])
            try:
                if not given_address:
                    raise ValueError("Empty String")
                    return render_template("home_page.html")
                #create YandexGeolocationApi object with API KEY
                api_object=YandexGeolocationApi(yandex_api_key)

                #get geolocation of given address with get_geolocation method
                geolocation: tuple=api_object.get_geolocation(api_object.search_by_address(given_address))

                # creation of Distance object
                distance_object=Distance()
                result_list:list=distance_object.find_nearest_point_mkad(geolocation)
                #logging to a file
                logging.basicConfig(filename="output.log", filemode="a", encoding="utf-8",level=logging.INFO)
                result="Origin-->"+str(result_list[0:2])+" Destination-->"+str(result_list[2:4])+" Distance(KM)-->"+str(result_list[4:])
                logging.info(str(result))

                return render_template("home_page.html")

            # if not user enter nothing this code will be executed
            except ValueError as error:
                abort(400)

    # if html file  is not find in given address this code will be executed
    except TemplateNotFound:
        abort(404)
