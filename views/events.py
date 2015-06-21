__author__ = 'mms'

from datetime import datetime

from flask import Blueprint, render_template, request, redirect
from flask.ext.login import (current_user,fresh_login_required)
from models import models
from libs import tweets


events_app = Blueprint('events_app', __name__, template_folder='templates')


@events_app.route('/')
def index():
	data = {
		'events': models.Event.objects.order_by("-last_updated")
	}
	return render_template('index.html', **data)


@events_app.route("/events/create", methods=["GET", "POST"])
@fresh_login_required
def admin_entry_create():
	if request.method == "POST":
		event = models.Event()
		event.title = request.form.get('title')
		event.description = request.form.get('content')
		event.starting_at = datetime.strptime(request.form.get('starting_at'), '%Y-%m-%d %H:%M:%S')
		event.ending_at = datetime.strptime(request.form.get('ending_at'), '%Y-%m-%d %H:%M:%S')

		event.user = current_user.get_mongo_doc()
		event.save()

		#status = event.title + ' ' + event.description
		#if len(status) > 140: status = status[:137] + '...'
		#twitter.statuses.update(status)

		return redirect('/events/%s' % event.id)

	else:
		data = {
			'title': 'Create new event',
			'event': None
		}
		return render_template('/event/event_edit.html', **data)


@events_app.route("/events/<event_id>/edit", methods=["GET", "POST"])
@fresh_login_required
def admin_entry_edit(event_id):
	event = models.Event.objects().with_id(event_id)

	if event:
		if event.user.id != current_user.id:
			return render_template('event/event_edit.html',error="ERROR: You do not have permission to edit this event")

		if request.method == "POST":
			event.title = request.form.get('title', '')
			event.description = request.form.get('content')
			event.starting_at = datetime.strptime(request.form.get('starting_at'), '%Y-%m-%d %H:%M:%S')
			event.ending_at = datetime.strptime(request.form.get('ending_at'), '%Y-%m-%d %H:%M:%S')

			event.save()

			#flash('Event has been updated')

		data = {
			'title': 'Edit event',
			'event': event
		}

		return render_template('event/event_edit.html', **data)

	else:
		return render_template('event/event_edit.html', error="Unable to find entry %s".format(event_id))


@events_app.route('/events/<event_id>')
def entry_page(event_id):

	event = models.Event.objects().with_id(event_id)

	if event:

		ids = tweets.search() 	# tweets.search(query=event.title)
		data = {
			'event': event,
			'author': event.user,
			'tweet_ids': ids
		}
		return render_template('event/event_display.html', **data)

	else:
		return render_template('event/event_display.html', error="Event not found.")


@events_app.route('/events/<event_id>', methods=["POST"])
@fresh_login_required
def post_comment(event_id):
	event = models.Event.objects().with_id(event_id)

	if event:
		if request.method == "POST":
			comment = models.Comment()
			comment.author = current_user.email
			comment.body = request.form.get('body')

			event.comments.append(comment)
			event.save()
			# flash('Comment has been added')
			return redirect('/events/%s' % event.id)
	else:
		return render_template('event/event_display.html', error="Event not found.")

