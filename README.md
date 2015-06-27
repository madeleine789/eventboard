

## Eventboard App

### DONE
* register and login users
* create events 
* edit events
* comment events
* search tweets

### TO DO
* tests
* deployment on pythonanywhere.com

### Configure environment

* Set up MongoDB
* Download code 
* Create Git repo

		git init
		git add .
		git commit -am "init commit"

* Create virtual environment and install package requirements - in project directory run:

		pyconfig/config.sh

	or 

		pyconfig\config.bat

### Run MongoDB
        
        mongod
		
### Run Eventboard app
	
	python run.py

### Views

* / - index page - display list of all events. 
* /events/<event_id> - display event with <event_id>
* /events/<event_id>/edit - display edit page for event (event creator only)
* /profile - display current_user info
* /users/<user_id> - display user with <user_id>
* /register - create a new user
* /login - login with email and password
* /logout - logout user



