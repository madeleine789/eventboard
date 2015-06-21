__author__ = 'mms'

from app import app

from views.events import events_app
from views.auth import auth_app
from views.users import users_app

app.register_blueprint(events_app)
app.register_blueprint(auth_app)
app.register_blueprint(users_app)

if __name__ == "__main__":
	app.run(debug=True)