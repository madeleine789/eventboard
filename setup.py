__author__ = 'mms'

from setuptools import setup, find_packages

setup(
  name='eventboard',
  version='0.1.1',
  description='Flask web application',
  long_description=('Flask web application'),
  url='http://pypi.python.org/pypi/eventboard_v010/',
  license='MIT',
  author='mms',
  author_email='some_email@gmail.com',
  packages=find_packages(exclude=['flask*']),
  install_requires=["Flask==0.10.1",
		"flask-mongoengine==0.7.0",
		"Flask-Bcrypt",
		"flask-login==0.2.7",
		"pymongo==2.8",
		"flask-cache==0.13.1",
		"flask-wtf==0.11",
		"flask-twitter-oembedder==0.1.8",
		"twittersearch==1.0.1",
		"tweepy==3.3.0"
  ],
  include_package_data=True,
  entry_points = {
  'console_scripts': [ 'run_server = eventboard:run']
  },
  package_data={
    'static': 'eventboard/static/*',
    'templates': 'eventboard/templates/*'},

)