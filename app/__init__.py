from flask import Flask, render_template
from flask.ext.assets import Environment
from flask.ext.navigation import Navigation
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.config.from_object('app.config.default.DefaultConfig')
assets = Environment(app)
db = SQLAlchemy(app)
nav = Navigation(app)
toolbar = DebugToolbarExtension(app)


# Register blueprint modules
from app.modules.about.views import module as about_views
from app.modules.menu.views import module as menu_module
app.register_blueprint(about_views)
app.register_blueprint(menu_module)


# Navigation
main_navigation = nav.Bar('main', [
    nav.Item('Menu', 'menu.index'),
    nav.Item('About Lord Simeon', 'about.index'),
])


# This should move to an error module.
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
