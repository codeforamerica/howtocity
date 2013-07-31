import os
import json
from flask_oauth import OAuth

oauth = OAuth()

def load_service_config():
	with open('providers.json', 'r') as f:
		services = json.loads(f.read())
	return services

service_config = load_service_config()

def open_remote_oauth(service_name):
	''' Given string service_name, return an OAuth
		remote app for that service.

		Requires environment variables for remote
		app ids and secrets
	'''
	service_name = service_name.lower()
	token_params = {}
	for key, value in service_config[service_name]['request_token_params'].iteritems():
		token_params.update({key: value})

	service = oauth.remote_app(service_name,
		base_url=			service_config[service_name]['base_url'],
		request_token_url=	service_config[service_name]['request_token_url'],
		access_token_url=	service_config[service_name]['access_token_url'],
		authorize_url=		service_config[service_name]['authorize_url'],
		consumer_key=		os.environ[service_name.upper() + '_APP_ID'],
		consumer_secret=	os.environ[service_name.upper() + '_APP_SECRET'],
		request_token_params=token_params)

	return service

