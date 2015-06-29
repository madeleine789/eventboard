from views.auth import auth_app
from views.events import events_app
from views.users import users_app

__author__ = 'mms'

from werkzeug.contrib.profiler import ProfilerMiddleware
from app import app, cache

app.register_blueprint(events_app)
app.register_blueprint(auth_app)
app.register_blueprint(users_app)

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
if __name__ == "__main__":

	app.run( debug=True)

	with app.app_context():
		cache.clear()