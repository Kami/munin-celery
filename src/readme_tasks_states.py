"""=cut
=head1 NAME

celery_tasks_states - Munin plugin to monitor the number of Celery tasks in each state.

=head1 REQUIREMENTS

 - Python
 - celery (http://celeryproject.org/)
 - celerymon (http://github.com/ask/celerymon)

Note: don't forget to enable sending of the events on the celery daemon - run it with the --events option

=head1 CONFIGURATION

Default configuration:

  [celery_tasks_states]
	 env.api_url http://localhost:8989
	 env.workers all

If workers variable is not set or set to "all", task number for all the workers is monitored.

You can optionally set the workers variable to the string of hostnames you want to monitor separated by a comma.

For example:

  [celery_tasks]
	 env.workers localhost,foo.bar.net,bar.foo.net

This would only monitor the number of tasks for the workers with the hostnames "localhost", "foo.bar.net" and "bar.foo.net"

=head1 MAGIC MARKERS

  #%# family=manual
  #%# capabilities=autoconf

=head1 AUTHOR

Tomaz Muraus (http://github.com/Kami/munin-celery)

=head1 LICENSE

GPLv2

=cut"""

