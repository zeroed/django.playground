import os

__author__ = 'e.rossi'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Celery Settings
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

# RabbitMQ is the default broker
BROKER_URL = "amqp://guest:guest@localhost:5672//"

# List of modules to import when celery starts.
CELERY_IMPORTS = ("playground.tasks", "playground.jobs.mock")

CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}

# http://docs.celeryproject.org/en/latest/userguide/tasks.html#disable-rate-limits-if-they-re-not-used
CELERY_DISABLE_RATE_LIMITS = True

# Persisting results
# http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend

# Database
# CELERY_RESULT_BACKEND = 'db+scheme://user:password@host:port/dbname'
# CELERY_RESULT_BACKEND = 'db+sqlite:///' + os.path.join(BASE_DIR, 'results.sqlite3')
# - sqlite (filename) CELERY_RESULT_BACKEND = ‘db+sqlite:///results.sqlite’
# - mysql CELERY_RESULT_BACKEND = ‘db+mysql://scott:tiger@localhost/foo’
# - postgresql CELERY_RESULT_BACKEND = ‘db+postgresql://postgres:postgres@localhost/mydatabase’
# - oracle CELERY_RESULT_BACKEND = ‘db+oracle://scott:tiger@127.0.0.1:1521/sidname’

CELERY_RESULT_SERIALIZER = 'json'

# use custom table names for the database result backend.
TABLE_APP_NAME = 'foobardb'
CELERY_RESULT_DB_TABLENAMES = {
    'task': TABLE_APP_NAME + '_taskmeta',
    'group': TABLE_APP_NAME + '_groupmeta',
}

# echo enables verbose logging from SQLAlchemy.
CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}

## Using the database to store task state and results.
# CELERY_RESULT_BACKEND = "database"

# If you have trubles with psycopg2 on windows... use linux
CELERY_RESULT_BACKEND = 'db+postgresql://dbuser:dbpassword@localhost:5432/' + TABLE_APP_NAME
# ... and if you wanna a dirty trick:
# CELERY_RESULT_BACKEND = 'db+sqlite:///' + os.path.join(BASE_DIR, 'results.sqlite3')

# Django persistence
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
# using-the-django-orm-cache-as-a-result-backend
# For the database backend you must use:
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
# For the cache backend you can use:
# CELERY_RESULT_BACKEND = 'djcelery.backends.cache:CacheBackend'

# AMQP persistence
# http://docs.celeryproject.org/en/latest/configuration.html#amqp-backend-settings
# CELERY_RESULT_BACKEND = 'amqp'
# CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.

# Cache Memory persistence
# CELERY_RESULT_BACKEND = 'cache+memcached://127.0.0.1:11211/'

# Redis Backend persistence
# http://docs.celeryproject.org/en/latest/configuration.html#redis-backend-settings
# CELERY_RESULT_BACKEND = 'redis://:password@host:port/db'
# CELERY_RESULT_BACKEND = 'redis://localhost/0'

# MongoDB Backend persistence
# http://docs.celeryproject.org/en/latest/configuration.html#mongodb-backend-settings
# CELERY_RESULT_BACKEND = 'mongodb://192.168.1.100:30000/'
# CELERY_MONGODB_BACKEND_SETTINGS = {
#     'database': 'mydb',
#     'taskmeta_collection': 'my_taskmeta_collection',
# }

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
# using serializer name
# http://docs.celeryproject.org/en/latest/configuration.html#broker-settings
# or the actual content-type (MIME): ['application/json']
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = False

# Email address used as sender (From field).
SERVER_EMAIL = 'no-reply@foobar.org'

# Mailserver configuration
EMAIL_HOST = 'mail.foobar.org'
EMAIL_PORT = 25
# EMAIL_HOST_USER = 'servers'
# EMAIL_HOST_PASSWORD = 's3cr3t'

CELERY_ROUTES = {
    'tasks.add': 'low-priority',
}

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# http://docs.celeryproject.org/en/latest/userguide/monitoring.html
# http://docs.celeryproject.org/en/latest/userguide/monitoring.html#flower-real-time-celery-web-monitor
