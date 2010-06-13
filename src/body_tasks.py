def clean_task_name(task_name):
	return task_name.replace('.', '_')

# Config
def print_config(task_names):
	print 'graph_title Celery tasks'
	print 'graph_args --lower-limit 0'
	print 'graph_scale no'
	print 'graph_vlabel tasks per ${graph_period}'
	print 'graph_category celery'

	for name in task_names:
		print '%s.label %s' % (clean_task_name(name), name)
		print '%s.type DERIVE' % (clean_task_name(name))
		print '%s.min 0' % (clean_task_name(name))
		print '%s.info number of %s tasks' % (clean_task_name(name), name)
		
# Values
def print_values(task_names = None, api_url = None):
	for task_name in task_names:
		count = len(get_data('task_details', api_url, task_name))
		print '%s.value %d' % (clean_task_name(task_name), count)
		
if __name__ == '__main__':
	task_names = os.environ.get('tasks', None)
	api_url = os.environ.get('api_url', API_URL)
	
	check_web_server_status(api_url)
	
	if not task_names:
		print 'You need to define at least one task name'
		sys.exit(-1)
		
	task_names = task_names.split(',')
			
	if len(sys.argv) > 1:
		if sys.argv[1] == 'config':
			print_config(task_names)
		elif sys.argv[1] == 'autoconf':
			print 'yes'
	else:
		print_values(task_names, api_url)

