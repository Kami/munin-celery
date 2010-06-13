import os
import sys
import urllib

try:
	import json
except:
	import simplejson as json

API_URL = 'http://localhost:8989'
URL_ENDPOINTS = {
		'workers': '/api/worker/',
		'worker_tasks': '/api/worker/%s/tasks',
		'tasks': '/api/task/',
		'task_names': '/api/task/name/',
		'task_details': '/api/task/name/%s',
}
TASK_STATES = (
			'task-accepted',
			'task-received',
			'task-succeeded',
			'task-failed',
			'task-retried',
)

def get_data(what, api_url, *args):
	try:
		request = urllib.urlopen('%s%s' % (api_url, \
										   URL_ENDPOINTS[what] % (args)))
		response = request.read()
		return json.loads(response)
	except IOError:
		print 'Could not connect to the celerymon webserver'
		sys.exit(-1)
		
def check_web_server_status(api_url):
	try:
		request = urllib.urlopen(api_url)
		response = request.read()
	except IOError:
		print 'Could not connect to the celerymon webserver'
		sys.exit(-1)

