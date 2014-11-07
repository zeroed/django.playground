--------------
# YAF(Yet Another Foobar) in Python and Django
--------------

## Dependencies

- [Python 3.4.1 (Docs)](https://docs.python.org/3/)

    ... install Python in a way that you like... I don't care ...
    Also use [Virtualenv 1.11.6](http://virtualenv.readthedocs.org/en/latest/virtualenv.htm)
    
    `eddie@linuxbox:~/Workspace/django.playground$ source playground.env/bin/activate`

- [PiP](https://pip.pypa.io/en/latest/index.html)

    ```
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ python get-pip.py
    $ sudo pip install Django
    ```
    
- [Django 1.6.6](https://docs.djangoproject.com/en/1.6/)

    ```
    pip install Django==1.6.6
    python -c "import django; print(django.get_version())"
    > 1.6.6
    ```

    Do something...

    ```
    eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py syncdb
    Creating tables ...
    Creating table django_admin_log
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_groups
    Creating table auth_user_user_permissions
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table celery_taskmeta
    Creating table celery_tasksetmeta
    Creating table djcelery_intervalschedule
    Creating table djcelery_crontabschedule
    Creating table djcelery_periodictasks
    Creating table djcelery_periodictask
    Creating table djcelery_workerstate
    Creating table djcelery_taskstate
    Creating table playground_detector
    Creating table playground_result

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'eddie'):
    Email address:
    Password:
    Password (again):
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)
    eddie@linuxbox:~/Workspace/django.playground$
    ```
    
- [django-extensions/django-extensions](https://github.com/django-extensions/django-extensions)

    Can you seriously code without `python3 manage.py shell_plus --use-pythonrc` ? :hearts:

    ```
    $ pip install django-extensions
    ```
    

- [PostgreSQL](http://www.postgresql.org) adapter: [PsycoPG stable release (2.5.3)](http://initd.org/psycopg)

    Install on Linux:

    ```
    $ sudo service postgresql status|start|stop|restart
    9.3/main (port 5432): online
    ```

    On Windows:

    ```
    PS C:\WINDOWS\system32> net start postgresql-x64-9.3
    The postgresql-x64-9.3 - PostgreSQL Server 9.3 service is starting.
    The postgresql-x64-9.3 - PostgreSQL Server 9.3 service was started successfully.
    PS C:\WINDOWS\system32> net stop postgresql-x64-9.3
    The postgresql-x64-9.3 - PostgreSQL Server 9.3 service is stopping.
    The postgresql-x64-9.3 - PostgreSQL Server 9.3 service was stopped successfully.
    ```

    Configure PostgreSQL on Ubuntu:

    [guide on help.ubuntu](https://help.ubuntu.com/community/PostgreSQL)

    ```
      sudo apt-get install postgresql
      sudo apt-get install postgresql-client
      sudo apt-get install postgresql postgresql-contrib
      sudo apt-get install pgadmin3
      sudo touch /var/lib/postgresql/.psql_history
      sudo -u postgres psql postgres
      sudo -u postgres createuser dbuser
      sudo -u postgres createdb foobardb
    eddie@linuxbox:~/Workspace/django.playground$ sudo -u postgres psql postgres
    psql (9.3.5)
    Type "help" for help.
    postgres=# \password dbuser
    postgres=# grant all privileges on database foobardb to dbuser;
    GRANT
    postgres=#
    ```

    Getting the Admin console:

    ```
    eddie@linuxbox:~/Workspace/django.playground$ pgadmin3 &
    ```

- [PsycoPG version 2.5.3](http://initd.org/psycopg/)

    ```
    pip install psycopg2
    ```

- [Celery: Distributed Task Queue](http://www.celeryproject.org/)

    ```
    pip install -U Celery
        Successfully installed Celery billiard pytz kombu amqp anyjson
    pip install django-celery
        Successfully installed django-celery
    ```

- [Using CeleryCam](http://docs.celeryproject.org/en/latest/history/changelog-2.1.html?highlight=celerycam#v210-news)

    ```
    eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celerycam
    -> evcam: Taking snapshots with djcelery.snapshot.Camera (every 1.0 secs.)
    [2014-08-19 10:27:47,558: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
    ```

- [RabbitMQ 3.3.4](http://www.rabbitmq.com/)

    ```python
    BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    ```

    Manage the service:

    ```
    $ sudo apt-get install rabbitmq-server
    eddie@linuxbox:~/Workspace/django.playground$ sudo rabbitmq-plugins enable rabbitmq_management
    The following plugins have been enabled:
      mochiweb
      webmachine
      rabbitmq_web_dispatch
      amqp_client
      rabbitmq_management_agent
      rabbitmq_management
    Plugin configuration has changed. Restart RabbitMQ for changes to take effect.
    eddie@linuxbox:~/Workspace/django.playground$
    eddie@linuxbox:~/Workspace/django.playground$ sudo service rabbitmq-server restart
    $ sudo rabbitmqctl add_user myuser mypassword
    $ sudo rabbitmqctl add_vhost myvhost
    $ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
    ```

- [SQLAlchemy 0.9.7](http://www.sqlalchemy.org/)

    ```
    pip install sqlalchemy
    ```

## From shell


```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py runserver
Validating models...

0 errors found
August 19, 2014 - 10:26:18
Django version 1.6.5, using settings 'foobar.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[19/Aug/2014 10:26:28] "GET /admin/ HTTP/1.1" 200 1865
[19/Aug/2014 10:26:29] "POST /admin/ HTTP/1.1" 302 0
[19/Aug/2014 10:26:29] "GET /admin/ HTTP/1.1" 200 5103
[19/Aug/2014 10:26:32] "GET /admin/djcelery/taskstate/ HTTP/1.1" 200 4771
[19/Aug/2014 10:26:32] "GET /static/djcelery/style.css HTTP/1.1" 304 0
[19/Aug/2014 10:26:32] "GET /admin/jsi18n/ HTTP/1.1" 200 2344
[19/Aug/2014 10:26:35] "GET /admin/djcelery/workerstate/ HTTP/1.1" 200 2875
[19/Aug/2014 10:26:35] "GET /admin/jsi18n/ HTTP/1.1" 200 2344
[19/Aug/2014 10:26:38] "GET /admin/djcelery/crontabschedule/ HTTP/1.1" 200 2906
[19/Aug/2014 10:26:38] "GET /admin/jsi18n/ HTTP/1.1" 200 2344
```

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py shell                                                                                       │    sqlsequencereset
Python 3.4.0 (default, Apr 11 2014, 13:05:11)                                                                                                               │    startapp
[GCC 4.8.2] on linux                                                                                                                                        │    startproject
Type "help", "copyright", "credits" or "license" for more information.                                                                                      │    syncdb
(InteractiveConsole)                                                                                                                                        │    test
>>>                                                                                                                                                         │    testserver
```

## SQLall

Playground

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py sqlall playground
```

Result SQL:

```sql
BEGIN;
CREATE TABLE "playground_detector" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL,
    "description" varchar(1000) NOT NULL,
    "last_run_date" timestamp with time zone NOT NULL,
    "run_count" integer NOT NULL,
    "creation_date" timestamp with time zone NOT NULL
)
;
CREATE TABLE "playground_result" (
    "id" serial NOT NULL PRIMARY KEY,
    "detector_id" integer NOT NULL REFERENCES "playground_detector" ("id") DEFERRABLE INITIALLY DEFERRED,
    "content" varchar(1000) NOT NULL,
    "value" integer NOT NULL,
    "creation_date" timestamp with time zone NOT NULL
)
;
CREATE INDEX "playground_result_detector_id" ON "playground_result" ("detector_id");

COMMIT;
```

Celery (Django Celery)

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py sqlall djcelery
```

Resulting in:

```sql
BEGIN;
CREATE TABLE "celery_taskmeta" (
    "id" serial NOT NULL PRIMARY KEY,
    "task_id" varchar(255) NOT NULL UNIQUE,
    "status" varchar(50) NOT NULL,
    "result" text,
    "date_done" timestamp with time zone NOT NULL,
    "traceback" text,
    "hidden" boolean NOT NULL,
    "meta" text
)
;
CREATE TABLE "celery_tasksetmeta" (
    "id" serial NOT NULL PRIMARY KEY,
    "taskset_id" varchar(255) NOT NULL UNIQUE,
    "result" text NOT NULL,
    "date_done" timestamp with time zone NOT NULL,
    "hidden" boolean NOT NULL
)
;
CREATE TABLE "djcelery_intervalschedule" (
    "id" serial NOT NULL PRIMARY KEY,
    "every" integer NOT NULL,
    "period" varchar(24) NOT NULL
)
;
CREATE TABLE "djcelery_crontabschedule" (
    "id" serial NOT NULL PRIMARY KEY,
    "minute" varchar(64) NOT NULL,
    "hour" varchar(64) NOT NULL,
    "day_of_week" varchar(64) NOT NULL,
    "day_of_month" varchar(64) NOT NULL,
    "month_of_year" varchar(64) NOT NULL
)
;
CREATE TABLE "djcelery_periodictasks" (
    "ident" smallint NOT NULL PRIMARY KEY,
    "last_update" timestamp with time zone NOT NULL
)
;
CREATE TABLE "djcelery_periodictask" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL UNIQUE,
    "task" varchar(200) NOT NULL,
    "interval_id" integer REFERENCES "djcelery_intervalschedule" ("id") DEFERRABLE INITIALLY DEFERRED,
    "crontab_id" integer REFERENCES "djcelery_crontabschedule" ("id") DEFERRABLE INITIALLY DEFERRED,
    "args" text NOT NULL,
    "kwargs" text NOT NULL,
    "queue" varchar(200),
    "exchange" varchar(200),
    "routing_key" varchar(200),
    "expires" timestamp with time zone,
    "enabled" boolean NOT NULL,
    "last_run_at" timestamp with time zone,
    "total_run_count" integer CHECK ("total_run_count" >= 0) NOT NULL,
    "date_changed" timestamp with time zone NOT NULL,
    "description" text NOT NULL
)
;
CREATE TABLE "djcelery_workerstate" (
    "id" serial NOT NULL PRIMARY KEY,
    "hostname" varchar(255) NOT NULL UNIQUE,
    "last_heartbeat" timestamp with time zone
)
;
CREATE TABLE "djcelery_taskstate" (
    "id" serial NOT NULL PRIMARY KEY,
    "state" varchar(64) NOT NULL,
    "task_id" varchar(36) NOT NULL UNIQUE,
    "name" varchar(200),
    "tstamp" timestamp with time zone NOT NULL,
    "args" text,
    "kwargs" text,
    "eta" timestamp with time zone,
    "expires" timestamp with time zone,
    "result" text,
    "traceback" text,
    "runtime" double precision,
    "retries" integer NOT NULL,
    "worker_id" integer REFERENCES "djcelery_workerstate" ("id") DEFERRABLE INITIALLY DEFERRED,
    "hidden" boolean NOT NULL
)
;
CREATE INDEX "celery_taskmeta_task_id_like" ON "celery_taskmeta" ("task_id" varchar_pattern_ops);
CREATE INDEX "celery_taskmeta_hidden" ON "celery_taskmeta" ("hidden");
CREATE INDEX "celery_tasksetmeta_taskset_id_like" ON "celery_tasksetmeta" ("taskset_id" varchar_pattern_ops);
CREATE INDEX "celery_tasksetmeta_hidden" ON "celery_tasksetmeta" ("hidden");
CREATE INDEX "djcelery_periodictask_name_like" ON "djcelery_periodictask" ("name" varchar_pattern_ops);
CREATE INDEX "djcelery_periodictask_interval_id" ON "djcelery_periodictask" ("interval_id");
CREATE INDEX "djcelery_periodictask_crontab_id" ON "djcelery_periodictask" ("crontab_id");
CREATE INDEX "djcelery_workerstate_hostname_like" ON "djcelery_workerstate" ("hostname" varchar_pattern_ops);
CREATE INDEX "djcelery_workerstate_last_heartbeat" ON "djcelery_workerstate" ("last_heartbeat");
CREATE INDEX "djcelery_taskstate_state" ON "djcelery_taskstate" ("state");
CREATE INDEX "djcelery_taskstate_state_like" ON "djcelery_taskstate" ("state" varchar_pattern_ops);
CREATE INDEX "djcelery_taskstate_task_id_like" ON "djcelery_taskstate" ("task_id" varchar_pattern_ops);
CREATE INDEX "djcelery_taskstate_name" ON "djcelery_taskstate" ("name");
CREATE INDEX "djcelery_taskstate_name_like" ON "djcelery_taskstate" ("name" varchar_pattern_ops);
CREATE INDEX "djcelery_taskstate_tstamp" ON "djcelery_taskstate" ("tstamp");
CREATE INDEX "djcelery_taskstate_worker_id" ON "djcelery_taskstate" ("worker_id");
CREATE INDEX "djcelery_taskstate_hidden" ON "djcelery_taskstate" ("hidden");

COMMIT;
```

## RabbitMQ Service


On Linux:

```
eddie@linuxbox:~/Workspace/django.playground$ sudo service rabbitmq-server status
Status of node rabbit@linuxbox ...
Error: unable to connect to node rabbit@linuxbox: nodedown

DIAGNOSTICS
===========

attempted to contact: [rabbit@linuxbox]

rabbit@linuxbox:
  * connected to epmd (port 4369) on linuxbox
  * epmd reports: node 'rabbit' not running at all
                  no other nodes on linuxbox
  * suggestion: start the node
  
  current node details:                                                                                   
- node name: rabbitmqctl8550@linuxbox
- home dir: /var/lib/rabbitmq
- cookie hash: XDLsoUi+UetOP7SztXhjhw==

eddie@linuxbox:~/Workspace/django.playground$ sudo service rabbitmq-server start
 * Starting message broker rabbitmq-server
   ...done.     

eddie@linuxbox:~/Workspace/django.playground$ sudo rabbitmqctl status
Status of node rabbit@linuxbox ...
[{pid,2092},
 {running_applications,[{rabbit,"RabbitMQ","3.3.5"},
                        {os_mon,"CPO  CXC 138 46","2.2.14"},
                        {mnesia,"MNESIA  CXC 138 12","4.11"},
                        {xmerl,"XML parser","1.3.5"},
                        {sasl,"SASL  CXC 138 11","2.3.4"},
                        {stdlib,"ERTS  CXC 138 10","1.19.4"},
                        {kernel,"ERTS  CXC 138 10","2.16.4"}]},
 {os,{unix,linux}},
 {erlang_version,"Erlang R16B03 (erts-5.10.4) [source] [64-bit] [smp:4:4] [async-threads:30] [kernel-poll:true]\n"},
 {memory,[{total,40898920},
          {connection_procs,71696},
          {queue_procs,14544},
          {plugins,0},
          {other_proc,13377200},
          {mnesia,63920},
          {mgmt_db,0},
          {msg_index,31200},
          {other_ets,771600},
          {binary,5269296},
          {code,16395458},
          {atom,594537},
          {other_system,4309469}]},
 {alarms,[]},
 {listeners,[{clustering,25672,"::"},{amqp,5672,"::"}]},
 {vm_memory_high_watermark,0.4},
 {vm_memory_limit,1610298163},
 {disk_free_limit,50000000},
 {disk_free,29136732160},
 {file_descriptors,[{total_limit,924},
                    {total_used,5},
                    {sockets_limit,829},
                    {sockets_used,3}]},
 {processes,[{limit,1048576},{used,147}]},
 {run_queue,0},
 {uptime,9664}]
...done.
```

On windows:

```
\RabbitMQ Server\rabbitmq_server-3.3.4\sbin> .\rabbitmq-service status

*********************
Service control usage
*********************

rabbitmq-service help    - Display this help
rabbitmq-service install - Install the RabbitMQ service
rabbitmq-service remove  - Remove the RabbitMQ service

The following actions can also be accomplished by using
Windows Services Management Console (services.msc):

rabbitmq-service start   - Start the RabbitMQ service
rabbitmq-service stop    - Stop the RabbitMQ service
rabbitmq-service disable - Disable the RabbitMQ service
rabbitmq-service enable  - Enable the RabbitMQ service

PS C:\Program Files (x86)\RabbitMQ Server\rabbitmq_server-3.3.4\sbin> .\rabbitmq-service.bat stop
C:\Program Files\erl6.1\erts-6.1\bin\erlsrv: Service RabbitMQ stopped.
PS C:\Program Files (x86)\RabbitMQ Server\rabbitmq_server-3.3.4\sbin> .\rabbitmq-service.bat start
```

----------------
# Celery and RabbitMQ
----------------

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery -A foobar worker -l INFO -c 5
 
 -------------- celery@linuxbox v3.1.13 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-3.13.0-34-generic-x86_64-with-Ubuntu-14.04-trusty
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         foobar:0x7f57359a04e0
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     db+postgresql://dbuser:dbpassword@localhost:5432/foobardb
- *** --- * --- .> concurrency: 5 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . foobar.celery.debug_task
  . playground.tasks.mul
  . playground.tasks.xsum
  . tasks.add
  . tasks.slow_add

[2014-08-19 14:01:25,319: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2014-08-19 14:01:25,338: INFO/MainProcess] mingle: searching for neighbors
[2014-08-19 14:01:26,361: INFO/MainProcess] mingle: all alone
[2014-08-19 14:01:26,383: WARNING/MainProcess] celery@linuxbox ready.
[2014-08-19 14:02:26,064: INFO/MainProcess] Received task: tasks.slow_add[780985d3-98ff-4acd-955d-97012bea1aab]
[2014-08-19 14:02:26,065: INFO/MainProcess] Received task: tasks.slow_add[e52132a1-3059-4d34-8f77-548e7d01797d]
[2014-08-19 14:02:26,068: INFO/MainProcess] Received task: tasks.slow_add[591f199b-654b-47b1-a250-2d4a7e16f503]
[2014-08-19 14:02:29,073: INFO/MainProcess] Received task: tasks.slow_add[5fe3d6b1-8bb2-415a-8d6a-ae328c3daf65]
[2014-08-19 14:02:29,074: INFO/MainProcess] Received task: tasks.slow_add[59ad9020-358f-4db9-a59d-e2514c574aee]
[2014-08-19 14:02:29,076: INFO/MainProcess] Received task: tasks.slow_add[698041dc-21f6-4756-bfd9-ba61389672df]
[2014-08-19 14:02:56,091: INFO/Worker-1] tasks.slow_add[591f199b-654b-47b1-a250-2d4a7e16f503]: Adding 10 + 1 with delay 30
[2014-08-19 14:02:56,091: INFO/Worker-4] tasks.slow_add[e52132a1-3059-4d34-8f77-548e7d01797d]: Adding 10 + 1 with delay 30
[2014-08-19 14:02:56,096: INFO/Worker-2] tasks.slow_add[780985d3-98ff-4acd-955d-97012bea1aab]: Adding 10 + 1 with delay 30
[2014-08-19 14:02:56,382: INFO/MainProcess] Task tasks.slow_add[e52132a1-3059-4d34-8f77-548e7d01797d] succeeded in 30.31600374700065s: 11
[2014-08-19 14:02:56,393: INFO/MainProcess] Task tasks.slow_add[591f199b-654b-47b1-a250-2d4a7e16f503] succeeded in 30.32354598799793s: 11
[2014-08-19 14:02:56,394: INFO/MainProcess] Task tasks.slow_add[780985d3-98ff-4acd-955d-97012bea1aab] succeeded in 30.328204088997154s: 11
[2014-08-19 14:03:26,411: INFO/Worker-4] tasks.slow_add[59ad9020-358f-4db9-a59d-e2514c574aee]: Adding 10 + 1 with delay 30
[2014-08-19 14:03:26,421: INFO/Worker-1] tasks.slow_add[698041dc-21f6-4756-bfd9-ba61389672df]: Adding 10 + 1 with delay 30
[2014-08-19 14:03:26,426: INFO/Worker-2] tasks.slow_add[5fe3d6b1-8bb2-415a-8d6a-ae328c3daf65]: Adding 10 + 1 with delay 30
[2014-08-19 14:03:26,461: INFO/MainProcess] Task tasks.slow_add[698041dc-21f6-4756-bfd9-ba61389672df] succeeded in 30.06820341400089s: 11
[2014-08-19 14:03:26,471: INFO/MainProcess] Task tasks.slow_add[59ad9020-358f-4db9-a59d-e2514c574aee] succeeded in 30.088866437999968s: 11
[2014-08-19 14:03:26,471: INFO/MainProcess] Task tasks.slow_add[5fe3d6b1-8bb2-415a-8d6a-ae328c3daf65] succeeded in 30.07693877800193s: 11

```
    
----------------
# Celery controls
----------------

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery

Usage: manage.py celery <command> [options] 

Show help screen and exit.

Options:
  -A APP, --app=APP     app instance to use (e.g. module.attr_name)
  -b BROKER, --broker=BROKER
                        url to broker.  default is 'amqp://guest@localhost//'
  --loader=LOADER       name of custom loader class to use.
  --config=CONFIG       Name of the configuration module
  --workdir=WORKING_DIRECTORY
                        Optional directory to change to after detaching.
  -C, --no-color        
  -q, --quiet           
  --version             show program's version number and exit
  -h, --help            show this help message and exit

---- -- - - ---- Commands- -------------- --- ------------

+ Main: 
|    celery worker
|    celery events
|    celery beat
|    celery shell
|    celery multi
|    celery amqp

+ Remote Control: 
|    celery status
 
|    celery inspect --help
|    celery inspect active
|    celery inspect active_queues
|    celery inspect clock
|    celery inspect conf None
|    celery inspect memdump
|    celery inspect memsample
|    celery inspect objgraph None
|    celery inspect ping
|    celery inspect registered
|    celery inspect report
|    celery inspect reserved
|    celery inspect revoked
|    celery inspect scheduled
|    celery inspect stats
 
|    celery control --help
|    celery control add_consumer <queue> [exchange [type [routing_key]]]
|    celery control autoscale [max] [min]
|    celery control cancel_consumer <queue>
|    celery control disable_events
|    celery control enable_events
|    celery control pool_grow [N=1]
|    celery control pool_shrink [N=1]
|    celery control rate_limit <task_name> <rate_limit> (e.g. 5/s | 5/m | 5/h)>
|    celery control time_limit <task_name> <soft_secs> [hard_secs]

+ Utils: 
|    celery purge
|    celery list
|    celery migrate
|    celery call
|    celery result
|    celery report
---- -- - - --------- -- - -------------- --- ------------
```

Start the beat periodic task scheduler.

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celerybeat -l INFO
celery beat v3.1.13 (Cipater) is starting.
__    -    ... __   -        _
Configuration ->
    . broker -> amqp://guest:**@localhost:5672//
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> now (0s)
[2014-08-19 14:29:18,839: INFO/MainProcess] beat: Starting...
```

## Admin panel

Do not forget to start the `celerycam` to view the tasks status on your [admin page](http://localhost:8000/admin/djcelery/taskstate/):

```
$ python3 manage.py celerycam --verbosity=3 --frequency=1 --loglevel=INFO
```

Docs for [celerycam](http://docs.celeryproject.org/en/latest/history/changelog-2.1.html?highlight=celerycam#v210-news).

## Check if everything is up 'n' running

```
eddie@linuxbox:~/Workspace/django.playground$ sudo service postgresql status
9.3/main (port 5432): online

eddie@linuxbox:~/Workspace/django.playground$ sudo service rabbitmq-server status
Status of node rabbit@linuxbox ...
[{pid,8659},
 {running_applications,
     [{rabbitmq_management,"RabbitMQ Management Console","3.3.5"},
      {rabbitmq_web_dispatch,"RabbitMQ Web Dispatcher","3.3.5"},
      {webmachine,"webmachine","1.10.3-rmq3.3.5-gite9359c7"},
      {mochiweb,"MochiMedia Web Server","2.7.0-rmq3.3.5-git680dba8"},
      {rabbitmq_management_agent,"RabbitMQ Management Agent","3.3.5"},
      {rabbit,"RabbitMQ","3.3.5"},
      {os_mon,"CPO  CXC 138 46","2.2.14"},
      {inets,"INETS  CXC 138 49","5.9.7"},
      {mnesia,"MNESIA  CXC 138 12","4.11"},
      {amqp_client,"RabbitMQ AMQP Client","3.3.5"},
      {xmerl,"XML parser","1.3.5"},
      {sasl,"SASL  CXC 138 11","2.3.4"},
      {stdlib,"ERTS  CXC 138 10","1.19.4"},
      {kernel,"ERTS  CXC 138 10","2.16.4"}]},
 ...
 
 eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery beat -l INFO --app=foobar &
[1] 9301
eddie@linuxbox:~/Workspace/django.playground$ celery beat v3.1.13 (Cipater) is starting.
__    -    ... __   -        _
Configuration ->
    . broker -> amqp://guest:**@localhost:5672//
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> now (0s)
[2014-08-20 07:49:59,796: INFO/MainProcess] beat: Starting...

eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celerycam --verbosity=3 --frequency=1 --loglevel=INFO &
[2] 9315
eddie@linuxbox:~/Workspace/django.playground$ -> evcam: Taking snapshots with djcelery.snapshot.Camera (every 1.0 secs.)
[2014-08-20 07:50:16,650: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
```

Check the Celery status:

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery report

software -> celery:3.1.13 (Cipater) kombu:3.0.21 py:3.4.0
            billiard:3.3.0.18 py-amqp:1.4.6
platform -> system:Linux arch:64bit, ELF imp:CPython
loader   -> celery.loaders.app.AppLoader
settings -> transport:amqp results:db+postgresql://dbuser:dbpassword@localhost:5432/foobardb

EMAIL_PORT: 25
EMAIL_HOST: 'mail.foobar.org'
CELERY_RESULT_DB_TABLENAMES: {
 'group': 'foobardb_groupmeta', 'task': 'foobardb_taskmeta'}
CELERY_RESULT_ENGINE_OPTIONS: {
 'echo': True}
SERVER_EMAIL: 'no-reply@foobar.org'
CELERY_ROUTES: {
 'tasks.add': 'low-priority'}
CELERY_RESULT_SERIALIZER: 'json'
CELERY_DISABLE_RATE_LIMITS: True
CELERY_ACCEPT_CONTENT: ['json']
BASE_DIR: '/home/eddie/Workspace/django.playground'
TABLE_APP_NAME: 'foobardb'
CELERY_ANNOTATIONS: {
 'tasks.add': {'rate_limit': '10/s'}}
CELERY_SEND_TASK_ERROR_EMAILS: False
CELERY_RESULT_BACKEND: 'db+postgresql://dbuser:dbpassword@localhost:5432/foobardb'
CELERY_TASK_SERIALIZER: 'json'
CELERYBEAT_SCHEDULER: 'djcelery.schedulers.DatabaseScheduler'
BROKER_URL: 'amqp://guest:********@localhost:5672//'
```

## tl;dr

If you don't want to look at `runAllTheThings.sh` you can do this:

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py runserver
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery --app=foobar worker -l INFO --concurrency=5 --events --heartbeat-interval=5 --broker='amqp://guest:guest@localhost:5672//' --pidfile=pids/celeryd.pid --logfile=logs/celeryd.log --detach
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celerycam --verbosity=3 --frequency=1 --loglevel=INFO --broker='amqp://guest:guest@localhost:5672//' --pidfile=pids/celeryev.pid --logfile=logs/celeryev.log --detach
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery beat -l INFO --app=foobar --max-interval=1 --broker='amqp://guest:guest@localhost:5672//' --pidfile=pids/celerybeat.pid --logfile=logs/celerybeat.log --detach
```

Celery events 3.1.13 (Cipater)
```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py celery events --frequency=1 --loglevel=INFO --broker='amqp://guest:guest@localhost:5672//' --app=foobar
```

## Fixtures

Initialize the Detectors in the DB

```
eddie@linuxbox ~/workspace.python/django.playground (develop) $ python3 manage.py loaddata fixtures/initial_data.xml
Installed 2 object(s) from 1 fixture(s)  
```

## Run a sample

Put 3 (let's do three) jobs on queue...

```
eddie@linuxbox:~/Workspace/django.playground$ python3 manage.py runscript delay --script-args=3
```

## Screenshot Or It Didn't Happen

![Screenshot](screenshots/00.png)
![Screenshot](screenshots/01.png)
![Screenshot](screenshots/02.png)
![Screenshot](screenshots/03.png)
![Screenshot](screenshots/04.png)
![Screenshot](screenshots/05.png)
![Screenshot](screenshots/06.png)

## When the sh\*\* hits the fan

```python
import pdb; pdb.set_trace()
```

[source SO](http://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way/1118271#1118271)
