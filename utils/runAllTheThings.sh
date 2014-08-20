#!/bin/sh

cd ~/Workspace/django.playground

# eddie@linuxbox:~/Workspace/django.playground$
python3 manage.py runserver

# eddie@linuxbox:~/Workspace/django.playground$
python3 manage.py celery --app=foobar worker -l INFO --concurrency=5 --events --pidfile=pids/celeryd.pid --logfile=logs/celeryd.log --broker='amqp://guest:guest@localhost:5672//' --heartbeat-interval=5 --detach

# eddie@linuxbox:~/Workspace/django.playground$
# tail -f logs/celery.log

# eddie@linuxbox:~/Workspace/django.playground$
python3 manage.py celerycam --verbosity=3 --frequency=1 --loglevel=INFO --broker='amqp://guest:guest@localhost:5672//' --pidfile=pids/celeryev.pid --logfile=logs/celeryev.log --detach

# eddie@linuxbox:~/Workspace/django.playground$
python3 manage.py celery beat -l INFO --app=foobar --broker='amqp://guest:guest@localhost:5672//' --max-interval=1 --pidfile=pids/celerybeat.pid --logfile=logs/celerybeat.log --detach
