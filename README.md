--------------
# YAF(Yet Another Foobar) in Python and Django
--------------

## Dependencies

- (Python 3.4.1 (Docs))[https://docs.python.org/3/]

    ... install Python in a way that you like... I don't care ...

- (PiP)[https://pip.pypa.io/en/latest/index.html]

    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    sudo pip install Django
    
- (Django 1.6.5)[https://docs.djangoproject.com/en/1.6/]

    pip install Django==1.6.5
    python -c "import django; print(django.get_version())"
    1.6.5
    
- (PostgreSQL)[http://www.postgresql.org/] adapter: (PsycoPG stable release (2.5.3))[http://initd.org/psycopg/

    pip install psycopg2
    
- (Celery: Distributed Task Queue)[http://www.celeryproject.org/]

    pip install -U Celery
        Successfully installed Celery billiard pytz kombu amqp anyjson
    pip install django-celery
        Successfully installed django-celery

- (RabbitMQ 3.3.4)[http://www.rabbitmq.com/]
    
    $ sudo apt-get install rabbitmq-server
        
----------------
# From shell
----------------

    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py sqlall
    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py shell

----------------
# SQLall
----------------

Playground

    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py sqlall playground
    BEGIN;
    CREATE TABLE "playground_detector" (
        "id" integer NOT NULL PRIMARY KEY,
        "name" varchar(200) NOT NULL,
        "description" varchar(1000) NOT NULL,
        "last_run_date" datetime NOT NULL,
        "run_count" integer NOT NULL,
        "creation_date" datetime NOT NULL
    )
    ;
    CREATE TABLE "playground_result" (
        "id" integer NOT NULL PRIMARY KEY,
        "detector_id" integer NOT NULL REFERENCES "playground_detector" ("id"),
        "content" varchar(1000) NOT NULL,
        "value" integer NOT NULL,
        "creation_date" datetime NOT NULL
    )
    ;
    CREATE INDEX "playground_result_1141f28e" ON "playground_result" ("detector_id");
    
    COMMIT;

Celery (Django Celery)

    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py sqlall djcelery
    BEGIN;
    CREATE TABLE "celery_taskmeta" (
        "id" integer NOT NULL PRIMARY KEY,
        "task_id" varchar(255) NOT NULL UNIQUE,
        "status" varchar(50) NOT NULL,
        "result" text,
        "date_done" datetime NOT NULL,
        "traceback" text,
        "hidden" bool NOT NULL,
        "meta" text
    )
    ;
    CREATE TABLE "celery_tasksetmeta" (
        "id" integer NOT NULL PRIMARY KEY,
        "taskset_id" varchar(255) NOT NULL UNIQUE,
        "result" text NOT NULL,
        "date_done" datetime NOT NULL,
        "hidden" bool NOT NULL
    )
    ;
    CREATE TABLE "djcelery_intervalschedule" (
        "id" integer NOT NULL PRIMARY KEY,
        "every" integer NOT NULL,
        "period" varchar(24) NOT NULL
    )
    ;
    CREATE TABLE "djcelery_crontabschedule" (
        "id" integer NOT NULL PRIMARY KEY,
        "minute" varchar(64) NOT NULL,
        "hour" varchar(64) NOT NULL,
        "day_of_week" varchar(64) NOT NULL,
        "day_of_month" varchar(64) NOT NULL,
        "month_of_year" varchar(64) NOT NULL
    )
    ;
    CREATE TABLE "djcelery_periodictasks" (
        "ident" smallint NOT NULL PRIMARY KEY,
        "last_update" datetime NOT NULL
    )
    ;
    CREATE TABLE "djcelery_periodictask" (
        "id" integer NOT NULL PRIMARY KEY,
        "name" varchar(200) NOT NULL UNIQUE,
        "task" varchar(200) NOT NULL,
        "interval_id" integer REFERENCES "djcelery_intervalschedule" ("id"),
        "crontab_id" integer REFERENCES "djcelery_crontabschedule" ("id"),
        "args" text NOT NULL,
        "kwargs" text NOT NULL,
        "queue" varchar(200),
        "exchange" varchar(200),
        "routing_key" varchar(200),
        "expires" datetime,
        "enabled" bool NOT NULL,
        "last_run_at" datetime,
        "total_run_count" integer unsigned NOT NULL,
        "date_changed" datetime NOT NULL,
        "description" text NOT NULL
    )
    ;
    CREATE TABLE "djcelery_workerstate" (
        "id" integer NOT NULL PRIMARY KEY,
        "hostname" varchar(255) NOT NULL UNIQUE,
        "last_heartbeat" datetime
    )
    ;
    CREATE TABLE "djcelery_taskstate" (
        "id" integer NOT NULL PRIMARY KEY,
        "state" varchar(64) NOT NULL,
        "task_id" varchar(36) NOT NULL UNIQUE,
        "name" varchar(200),
        "tstamp" datetime NOT NULL,
        "args" text,
        "kwargs" text,
        "eta" datetime,
        "expires" datetime,
        "result" text,
        "traceback" text,
        "runtime" real,
        "retries" integer NOT NULL,
        "worker_id" integer REFERENCES "djcelery_workerstate" ("id"),
        "hidden" bool NOT NULL
    )
    ;
    CREATE INDEX "celery_taskmeta_2ff6b945" ON "celery_taskmeta" ("hidden");
    CREATE INDEX "celery_tasksetmeta_2ff6b945" ON "celery_tasksetmeta" ("hidden");
    CREATE INDEX "djcelery_periodictask_8905f60d" ON "djcelery_periodictask" ("interval_id");
    CREATE INDEX "djcelery_periodictask_7280124f" ON "djcelery_periodictask" ("crontab_id");
    CREATE INDEX "djcelery_workerstate_11e400ef" ON "djcelery_workerstate" ("last_heartbeat");
    CREATE INDEX "djcelery_taskstate_5654bf12" ON "djcelery_taskstate" ("state");
    CREATE INDEX "djcelery_taskstate_4da47e07" ON "djcelery_taskstate" ("name");
    CREATE INDEX "djcelery_taskstate_abaacd02" ON "djcelery_taskstate" ("tstamp");
    CREATE INDEX "djcelery_taskstate_cac6a03d" ON "djcelery_taskstate" ("worker_id");
    CREATE INDEX "djcelery_taskstate_2ff6b945" ON "djcelery_taskstate" ("hidden");
    
    COMMIT;