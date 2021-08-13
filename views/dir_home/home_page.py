from views.dir_home.__init__ import *

home_page = Blueprint('dir_home', __name__,
                      template_folder='templates',
                      static_folder='static')



@home_page.route('/',methods=["GET","POST"])
def home_page_function():
    try:
        if request.method=="GET":
            return render_template("home_page.html")
        elif request.method=="POST":
            address_data=request.form["address"]
            logging.basicConfig(filename='output.log', filemode='a',level=logging.INFO)
            logging.info('Started')
            logging.info('Finished')
            return address_data



    except TemplateNotFound:
        abort(404)