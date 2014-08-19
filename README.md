--------------
# YAF(Yet Another Foobar) in Python and Django
--------------

## Dependencies

- [Python 3.4.1 (Docs)](https://docs.python.org/3/)

    ... install Python in a way that you like... I don't care ...

- [PiP](https://pip.pypa.io/en/latest/index.html)

    `wget https://bootstrap.pypa.io/get-pip.py`
    `python get-pip.py`
    `sudo pip install Django`
    
- [Django 1.6.5](https://docs.djangoproject.com/en/1.6/)

    `pip install Django==1.6.5`

    `python -c "import django; print(django.get_version())"`

    `1.6.5`

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

    Check status and other stuff...

    ```
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

- [SQLAlchemy 0.9.7](http://www.sqlalchemy.org/)

    ```
    pip install sqlalchemy
    ```

----------------
# From shell
----------------

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

----------------
# From shell
----------------

    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py sqlall
    PS C:\Users\e.rossi\pythonWorkspace\foobar> python.exe .\manage.py shell

----------------
# SQLall
----------------

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

----------------
# RabbitMQ Service
----------------

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

----------------
# Celery and RabbitMQ
----------------
  
    \pythonWorkspace\foobar> celery.exe -A foobar worker -l info
    
     -------------- celery@E-ROSSI v3.1.13 (Cipater)
    ---- **** -----
    --- * ***  * -- Windows-8-6.2.9200
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         foobar:0x303a5f0
    - ** ---------- .> transport:   amqp://guest:**@localhost:5672//
    - ** ---------- .> results:     amqp
    - *** --- * --- .> concurrency: 4 (prefork)
    -- ******* ----
    --- ***** ----- [queues]
     -------------- .> celery           exchange=celery(direct) key=celery
    
    
    [tasks]
      . foobar.celery.debug_task
      . playground.tasks.add
      . playground.tasks.mul
      . playground.tasks.slow_add
      . playground.tasks.xsum
    
    [2014-08-18 15:26:54,830: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
    [2014-08-18 15:26:54,857: INFO/MainProcess] mingle: searching for neighbors
    [2014-08-18 15:26:55,874: INFO/MainProcess] mingle: all alone
    [2014-08-18 15:26:55,902: WARNING/MainProcess] celery@E-ROSSI ready.
    [2014-08-18 15:27:45,863: INFO/MainProcess] Received task: playground.tasks.slow_add[0a1b9b81-ae8f-4011-a0bd-9c90da68983f]
    [2014-08-18 15:27:47,049: INFO/MainProcess] Received task: playground.tasks.slow_add[4645856b-2e9b-4e5c-a7e5-60f3de89580c]
    [2014-08-18 15:27:48,094: INFO/MainProcess] Received task: playground.tasks.slow_add[9a1f6bdc-bdad-4b06-af01-ed28f0ef71dc]
    [2014-08-18 15:27:48,941: INFO/MainProcess] Task playground.tasks.slow_add[0a1b9b81-ae8f-4011-a0bd-9c90da68983f] succeeded in 3.077999999997701s: 11
    [2014-08-18 15:27:49,121: INFO/MainProcess] Received task: playground.tasks.slow_add[1d2c8b96-1b12-46e0-9350-209e5d7db0fd]
    [2014-08-18 15:27:50,152: INFO/MainProcess] Task playground.tasks.slow_add[4645856b-2e9b-4e5c-a7e5-60f3de89580c] succeeded in 3.1090000000003783s: 11
    [2014-08-18 15:27:50,206: INFO/MainProcess] Received task: playground.tasks.slow_add[c9392c5e-c6e6-4c68-8075-f36fdf1597f0]
    [2014-08-18 15:27:51,103: INFO/MainProcess] Received task: playground.tasks.slow_add[5d4a6829-c0e7-4ff7-949a-acb43d1ce4ce]
    [2014-08-18 15:27:51,230: INFO/MainProcess] Task playground.tasks.slow_add[9a1f6bdc-bdad-4b06-af01-ed28f0ef71dc] succeeded in 3.1409999999996217s: 11
    [2014-08-18 15:27:52,020: INFO/MainProcess] Received task: playground.tasks.slow_add[ea8f9472-5914-41ab-8dce-be576d035baa]
    [2014-08-18 15:27:52,196: INFO/MainProcess] Task playground.tasks.slow_add[1d2c8b96-1b12-46e0-9350-209e5d7db0fd] succeeded in 3.077999999997701s: 11
    [2014-08-18 15:27:52,918: INFO/MainProcess] Received task: playground.tasks.slow_add[d3c8fe29-07d0-492c-8fa3-dcd5f3c8d5a5]
    [2014-08-18 15:27:53,264: INFO/MainProcess] Task playground.tasks.slow_add[c9392c5e-c6e6-4c68-8075-f36fdf1597f0] succeeded in 3.062000000001717s: 11
    [2014-08-18 15:27:54,229: INFO/MainProcess] Task playground.tasks.slow_add[5d4a6829-c0e7-4ff7-949a-acb43d1ce4ce] succeeded in 3.125s: 11
    [2014-08-18 15:27:55,096: INFO/MainProcess] Task playground.tasks.slow_add[ea8f9472-5914-41ab-8dce-be576d035baa] succeeded in 3.0780000000013388s: 11
    [2014-08-18 15:27:55,997: INFO/MainProcess] Task playground.tasks.slow_add[d3c8fe29-07d0-492c-8fa3-dcd5f3c8d5a5] succeeded in 3.0780000000013388s: 11
    
----------------
# RabbitMQ console
----------------

    \RabbitMQ Server\rabbitmq_server-3.3.4\sbin> .\rabbitmq-plugins.bat enable rabbitmq_management
    
    The following plugins have been enabled:
      mochiweb
      webmachine
      rabbitmq_web_dispatch
      amqp_client
      rabbitmq_management_agent
      rabbitmq_management
    Plugin configuration has changed. Restart RabbitMQ for changes to take effect.
    
Console link: http://localhost:15672/#/
    
        guest/guest
    
    
