__author__ = 'mms'

from locust import HttpLocust, TaskSet, task
from random import randint, SystemRandom
from string import digits, ascii_uppercase
import random
def login(slf):
    slf.client.post("/login", data={'email': 'ledge@mail.com', 'password': '123'})

def post_comment(slf):
    body = ''.join(SystemRandom().choice(ascii_uppercase + digits) for _ in range(12))
    slf.client.post("/events/558eb817f18b3023b4c54167", data={'body': body})


def edit_event(slf):
    content = ''.join(SystemRandom().choice(ascii_uppercase + digits) for _ in range(128))
    slf.client.post("/events/558eb817f18b3023b4c54167/edit",
                    data={'content': content})


def post_event(slf):
    title = ''.join(SystemRandom().choice(ascii_uppercase + digits) for _ in range(20))
    content = ''.join(SystemRandom().choice(ascii_uppercase + digits) for _ in range(128))
    slf.client.post("/events/create", data={'title': title, 'content': content,
                                            'starting_at': '2015-07-01 11:00:00', 'ending_at': '2015-07-01 20:00:00'})


def index(slf):
    slf.client.get("/")


def get_login(slf):
    slf.client.get("/login")


def get_register(slf):
    slf.client.get("/register")

def get_event(slf):
    slf.client.get("/events/558eb817f18b3023b4c54167")

class UserBehavior(TaskSet):
    tasks = {index:2, get_login:2, get_register:2, get_event:2, post_event:1, post_comment:1}

    def on_start(self):
        login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 1000
    max_wait = 15000
