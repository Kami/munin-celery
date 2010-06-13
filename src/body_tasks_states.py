def clean_state_name(state_name):
	return state_name.replace('task-', '')

# Config
def print_config(workers = None):
	if workers:
		print 'graph_title Celery tasks in each state [workers = %s]' % (', ' . join(workers))
	else:
		print 'graph_title Celery tasks in each state'
	print 'graph_args --lower-limit 0'
	print 'graph_scale no'
	print 'graph_vlabel tasks per ${graph_period}'
	print 'graph_category celery'

	for name in TASK_STATES:
		name = clean_state_name(name)
		print '%s.label %s' % (name, name)
		print '%s.type DERIVE' % (name)
		print '%s.min 0' % (name)
		print '%s.info number of %s tasks' % (name, name)

# Values
def print_values(workers = None, api_url = None):
	data = get_data('tasks', api_url)
	
	counters = dict([(key, 0) for key in TASK_STATES])
	for task_name, task_data in data.iteritems():
		for entry in task_data:
			if not entry.get('state', None):
				continue
			
			state = entry.get('state', None)
			hostname = entry.get('hostname', None)
			
			if workers and hostname not in workers:
				continue
			
			counters[state] += 1
			
	for name in TASK_STATES:
		name_cleaned = clean_state_name(name)
		value = counters[name]
		print '%s.value %d' % (name_cleaned, value)
		
if __name__ == '__main__':
	workers = os.environ.get('workers', 'all')
	api_url = os.environ.get('api_url', API_URL)
	
	check_web_server_status(api_url)
	
	if workers in [None, '', 'all']:
		workers = None
	else:
		workers = workers.split(',')
			
	if len(sys.argv) > 1:
		if sys.argv[1] == 'config':
			print_config(workers)
		elif sys.argv[1] == 'autoconf':
			print 'yes'
	else:
		print_values(workers, api_url)
		
