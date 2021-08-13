from views.dir_home.__init__ import *

home_page = Blueprint('dir_home', __name__,
                      template_folder='templates',
                      static_folder='static')


@home_page.route('/')
def home_page_function():
    return render_template("home_page/home_page.html")