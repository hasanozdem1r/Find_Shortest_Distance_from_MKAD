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
            return request.form["address"]
    except TemplateNotFound:
        abort(404)