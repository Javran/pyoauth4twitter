# -*- coding: utf-8 -*-
from oauth.oauth_twitter import TwitterRequest, TwitterConsumer
import json

try:
	from config import CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL
	from config import ACCESS_TOKEN, ACCESS_SECRET
except:
	# required
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''

	# required if you want the demo of access_token obtaining
	CALLBACK_URL = ''

	# required if you want the demo of accessing user data only
	ACCESS_TOKEN = ''
	ACCESS_SECRET = ''

def obtain_token(tc):
	print "Step #1: request_token"
	tc.request_token()

	print "Step #2: authorize"
	tc.authorize()
	
	print "Step #3: access_token"
	tc.access_token()

def access_userdata(tc):
	print "Acquiring @twitter's profile..."	
	response = tc.request("GET", "https://api.twitter.com/1.1/users/show.json?screen_name=twitter" )
	jdata = json.load( response )
	print json.dumps( jdata, sort_keys = True, indent=4 )

if __name__ == '__main__':
	tc = TwitterConsumer(
		CONSUMER_KEY, 
		CONSUMER_SECRET, 
		CALLBACK_URL,
		verbose=True)

	answer = raw_input( "Run access_token obtaining demo?(Y/n)" )
	if answer != 'n':
		obtain_token( tc )

	if not tc.has_user():
		tc.for_user(ACCESS_TOKEN, ACCESS_SECRET)

	answer = raw_input( "Run user data accessing demo?(Y/n)" )
	if answer != 'n':
		access_userdata( tc )
