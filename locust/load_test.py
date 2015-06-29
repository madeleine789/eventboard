__author__ = 'mms'

from locust import HttpLocust, TaskSet, task


class CommenterBehavior(TaskSet):
    def on_start(self):
        self.client.post("/login", data={'email': 'commenter@mail.com', 'password': '123'})

    @task
    def post_comment(self):
        self.client.post("/events/558ecb0df18b30233cafa6cd", data={'body': 'This is a comment, fascinating af.'})
        self.interrupt()

class CreatorBehavior(TaskSet):
    def on_start(self):
        self.client.post("/login", data={'email': 'creator@mail.com', 'password': '123'})

    @task
    def edit_event(self):
        self.client.post("/events/558ecb0df18b30233cafa6cd/edit", data={'content': 'This is new fascinating description #event'})
        self.interrupt()

    @task
    def post_event(self):
        self.client.post("/events/create", data={'title':'This is a title.','content':'describing event....', 'starting_at':'2015-07-01 11:00:00', 'ending_at':'2015-07-01 20:00:00'})
        self.interrupt()


class UserBehavior(TaskSet):
    tasks = {CreatorBehavior:5} # , CommenterBehavior:5}

    @task
    def index(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.get("/login")

    @task
    def register(self):
        self.client.get("/register")

    @task
    def get_event(self):
        self.client.get("/events/558ecb0df18b30233cafa6cd")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 1000
    max_wait = 15000
