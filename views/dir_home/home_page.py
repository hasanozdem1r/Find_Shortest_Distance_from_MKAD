from views.dir_home.__init__ import *
from dir_api.yandex_api import YandexGeolocationApi

home_page = Blueprint('dir_home', __name__, template_folder='templates', static_folder='static')


@home_page.route('/',methods=["GET","POST"])
def home_page_function():
    try:
        if request.method=="GET":
            return render_template("home_page.html")
        elif request.method=="POST":
            address_data=request.form["address"]
            object_api=YandexGeolocationApi("35253147-4db2-4d3a-8a22-b8be047d103f")
            geolocation=object_api.get_geolocation(object_api.search_by_address(address_data))
            geolocation=geolocation[1]+","+geolocation[0]
            return render_template("home_page.html")
    except TemplateNotFound:
        abort(404)
