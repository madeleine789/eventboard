__author__ = 'mms'

from TwitterSearch import *
from app import app


def search(query='cheeky nandos ledge banter', max=5):

	keywords = query.split()
	try:
		tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
		tso.set_keywords(keywords)  # let's define all words we would like to have a look for
		# tso.set_language('de')  # we want to see German tweets only
		# tso.set_include_entities(False)  # and don't give us all those entity information

		# it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
			consumer_key=app.config['TWITTER_CONSUMER_KEY'],
			consumer_secret=app.config['TWITTER_CONSUMER_SECRET'],
			access_token=app.config['TWITTER_ACCESS_TOKEN'],
			access_token_secret=app.config['TWITTER_TOKEN_SECRET']
		)
		results = []
		# this is where the fun actually starts :)
		for tweet in ts.search_tweets_iterable(tso):
			results.append(tweet['id'])
			#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
			max -= 1
			if not max: break

		#print results
		return results

	except TwitterSearchException as e:  # take care of all those ugly errors if there are some
		print(e)
