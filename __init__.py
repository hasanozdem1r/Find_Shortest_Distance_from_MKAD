from flask import Blueprint, render_template,Flask

from __init__ import *
from dir_home.home_page import home_page

app=Flask(__name__)
app.register_blueprint(blueprint=home_page)

if __name__=="__main__":
    app.run(debug=True)

