
"""=cut
=head1 NAME

celery_tasks - Munin plugin to monitor the number of Celery tasks with specified names.

=head1 REQUIREMENTS

 - Python
 - celery (http://celeryproject.org/)
 - celerymon (http://github.com/ask/celerymon)

Note: don't forget to enable sending of the events on the celery daemon - run it with the --events option

=head1 CONFIGURATION

Default configuration:

None

You must set the name of at least one task you want to monitor (multiple names are separated by a comma).

For example:

  [celery_tasks]
	 env.tasks myapp.tasks.SendEmailTask,myapp2.tasks.FetchUserDataTask

This would monitor the number of task for a task with name "myapp.tasks.SendEmailTask" and "myapp2.tasks.FetchUserDataTask".

=head1 MAGIC MARKERS

  #%# family=manual
  #%# capabilities=autoconf

=head1 AUTHOR

Tomaz Muraus (http://github.com/Kami/munin-celery)

=head1 LICENSE

GPLv2

=cut"""

