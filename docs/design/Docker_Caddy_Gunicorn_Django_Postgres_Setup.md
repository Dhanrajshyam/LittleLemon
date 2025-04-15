Idea:

Docker Container:
    Caddy - For Static file server and Reverse Proxy
    Gunicorn - For WSGI server
    Django - Main App
    Postgres - Backend DB

Finally Launcher Docker image to launch the application.

Guide Link: https://betterstack.com/community/guides/scaling-python/dockerize-django/

Running Django application Ubuntu by copying project folder from Windows drive location to Ubuntu

# Open Ubuntu WSL in Windows after installing Ubuntu. Open Powershell as Admin and run the below command

wsl -d Ubuntu
or
wsl -d Ubuntu-24.04 # my version

# Set Ubuntu as Your Default WSL Distro (Optional but helpful)

wsl --set-default Ubuntu

# Open Ubuntu in WSL, You should see a prompt like:

shyam@ubuntu:~$

# Update apt in Ubuntu

sudo apt update

# Install python3

sudo apt install python3

# confirm python installed 

python3 --version

then you should see something like this:
ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ python3 --version
Python 3.12.3

# Install pip

sudo apt install python3-pip

# Install Virtual environment from pip

sudo apt install python3-venv

# Optionally you can install all at once.

sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib curl

# Navigate to Where You Want the Project

cd ~
mkdir projects
cd projects

if you want to remove folder, run this command after moving one folder up - rm -rf ~/projects


# Copy the Project from Windows to WSL

if Your Django project is at:
D:\e-Learning\Coursera\Meta Back-End Developer Professional Certificate\Back-End Developer Capstone\projects\Django-Capstone-project\Littlelemon_Custom\LittleLemon

In Ubuntu WSL, run:
cp -r "/mnt/d/e-Learning/Coursera/Meta Back-End Developer Professional Certificate/Back-End Developer Capstone/projects/Django-Capstone-project/Littlelemon_Custom/LittleLemon" .

# Confirm It’s There

ls LittleLemon
You should see your Django project files (manage.py  requirements.txt  django_project/  restaurant/  ...)

# Set Up Virtual Environment

cd LittleLemon
python3 -m venv venv | python3 -m venv <virtual_environment_name>
source venv/bin/activate | source <virtual_environment_name>/bin/activate

if you want to remove virtual environment and start from fresh, run this command to remove venv - rm -rf venv

# Check virtual environment activation

which python

then you should see something like this:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ python3 -m venv venv
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ source venv/bin/activate
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ which python
/home/ubuntushyam/projects/LittleLemon/venv/bin/python
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ which pip
/home/ubuntushyam/projects/LittleLemon/venv/bin/pip

# Install Requirements | If you have requirements.txt:

pip install -r requirements.txt

then you should see something like:
Successfully installed argon2-cffi-23.1.0 argon2-cffi-bindings-21.2.0 asgiref-3.8.1 certifi-2025.1.31 cffi-1.17.1 charset-normalizer-3.4.1 colorama-0.4.6 defusedxml-0.7.1 dj-database-url-2.3.0 django-5.2 django-axes-7.0.2 django-debug-toolbar-5.0.1 django-extensions-3.2.3 djangorestframework-3.15.2 djangorestframework-csv-3.0.2 djangorestframework-simplejwt-5.5.0 djangorestframework-xml-2.0.0 drf-yasg-1.21.9 flake8-7.1.1 gunicorn-23.0.0 idna-3.10 inflection-0.5.1 iniconfig-2.0.0 load-dotenv-0.1.0 mccabe-0.7.0 packaging-24.2 pipfile-0.0.2 pluggy-1.5.0 psycopg-3.2.4 psycopg-binary-3.2.4 pycodestyle-2.12.1 pycparser-2.22 pyflakes-3.2.0 pyjwt-2.9.0 pytest-8.3.4 pytest-django-4.10.0 python-dotenv-1.0.1 pytz-2025.1 pyyaml-6.0.2 requests-2.32.3 sqlparse-0.5.3 toml-0.10.2 typing-extensions-4.12.2 tzdata-2025.1 uritemplate-4.1.1 urllib3-2.3.0 whitenoise-6.9.0

If not, Install Django and gunicorm - pip install django gunicorn | add dependency to pip freeze > requirements.txt

# Setup DB and update the settings. 

In my case settings already updated before copying to Ubuntu. So just running or starting the DB - Postgres in Docker Container

docker run --rm --name django-littlelemon-db --env POSTGRES_PASSWORD=admin --env POSTGRES_DB=django_littlelemon --volume django-pg-data:/var/lib/postgresql/data --publish 5432:5432 postgres:bookworm

# Run Migrations to create tables in DB as per Django models | Run Migrations (just in case)

python manage.py makemigrations
python manage.py migrate

# Check DB connection and tables

docker exec -it django-littlelemon-db psql -U postgres -d django_littlelemon

then you should see something like this:
django_littlelemon=#

then type \dt and enter to see the tables
django_littlelemon=# \dt

then you should see list of tables like this:
                         List of relations
 Schema |                  Name                  | Type  |  Owner
--------+----------------------------------------+-------+----------
 public | Restaurant_booking                     | table | postgres
 public | Restaurant_customuser                  | table | postgres
 public | Restaurant_customuser_groups           | table | postgres
 public | Restaurant_customuser_user_permissions | table | postgres
 public | Restaurant_holiday                     | table | postgres
 public | Restaurant_menu                        | table | postgres

# You can also create or update or delete tables manually in Postgres

Log into an interactive Postgres session by typing:
sudo -u postgres psql

create a database for your project:
CREATE DATABASE <myproject>; 

create a database user for our project. Make sure to select a secure password:
CREATE USER <myprojectuser> WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8'; # set the default character encoding to UTF-8, which Django expects.
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed'; # the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions.
ALTER ROLE myprojectuser SET timezone TO 'UTC'; # By default, Django projects will be set to use UTC

give the new user access to administer the new database:
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

exit out of the PostgreSQL prompt by typing:
\q

# Run Server to see everything works

python3 manage.py runserver

# Run server using gunicorn | gunicorn <project_name>.wsgi:application

gunicorn Littlelemon.wsgi:application
or
gunicorn --bind 0.0.0.0:8000 Littlelemon.wsgi:application


then you should see something like:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ gunicorn Littlelemon.wsgi:application
[2025-04-14 17:22:02 +0000] [3063] [INFO] Starting gunicorn 23.0.0
[2025-04-14 17:22:02 +0000] [3063] [INFO] Listening at: http://127.0.0.1:8000 (3063)
[2025-04-14 17:22:02 +0000] [3063] [INFO] Using worker: sync
[2025-04-14 17:22:02 +0000] [3064] [INFO] Booting worker with pid: 3064

When you visit http://localhost:8000 once again, you'll notice that the styles are not loading because while Django's runserver handles both dynamic content and static files in a single process, Gunicorn is designed to only process Python/WSGI requests. We can setup static file server usind Caddy and route other requests to gunicorn.

In case of issues like the port 8000 already in use, you can kill that service using 1. Get PID: lsof -i :8000 & Kill Service by PID: kill -9 <PID>:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ gunicorn Littlelemon.wsgi:application
[2025-04-14 17:19:13 +0000] [3048] [INFO] Starting gunicorn 23.0.0
[2025-04-14 17:19:13 +0000] [3048] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-04-14 17:19:13 +0000] [3048] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-04-14 17:19:14 +0000] [3048] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-04-14 17:19:14 +0000] [3048] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-04-14 17:19:15 +0000] [3048] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-04-14 17:19:15 +0000] [3048] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-04-14 17:19:16 +0000] [3048] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-04-14 17:19:16 +0000] [3048] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-04-14 17:19:17 +0000] [3048] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-04-14 17:19:17 +0000] [3048] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-04-14 17:19:18 +0000] [3048] [ERROR] Can't connect to ('127.0.0.1', 8000)
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ lsof -i :8000
COMMAND  PID        USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  3011 ubuntushyam    3u  IPv4 155382      0t0  TCP localhost:8000 (LISTEN)
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ kill -9 3011


# Handling static files with Caddy

Before you can serve static files with file server, you need to set up the STATIC_ROOT environmental variable which specifies where all the static files for your application is located:

Littlelemon/settings.py
-------------------------
. . .
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
. . .

# You can use VS Code (Best Experience) to make changes in the project folder and files

If you have VS Code installed, just open the whole project from WSL:
code .

VS Code will launch with your project opened inside WSL, allowing you to edit settings.py (and any file) seamlessly.

you should see something like this:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ code .
Installing VS Code Server for Linux x64 (4949701c880d4bdb949e3c0e6b400288da7f474b)
Downloading: 100%
Unpacking: 100%
Unpacked 2067 files and folders to /home/ubuntushyam/.vscode-server/bin/4949701c880d4bdb949e3c0e6b400288da7f474b.
Looking for compatibility check script at /home/ubuntushyam/.vscode-server/bin/4949701c880d4bdb949e3c0e6b400288da7f474b/bin/helpers/check-requirements.sh
Running compatibility check script
Compatibility check successful (0)

If code is not recognized, install the "Remote - WSL" extension in VS Code and make sure the code command is available in PATH from WSL.
or Use vim (for advanced users): vim Littlelemon/settings.py

# collect static files from all your applications into a single directory

python3 manage.py collectstatic

then you should see something like this:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ python3 manage.py collectstatic
System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory '/home/ubuntushyam/projects/LittleLemon/Restaurant/static' in the STATICFILES_DIRS setting does not exist.

253 static files copied to '/home/ubuntushyam/projects/LittleLemon/staticfiles'.

# proceed to set up Caddy through its Docker image

ensure port 80 isn't in use first
lsof -i :80

Once the static files have been copied over, you can proceed to set up Caddy through its Docker image by running the command below in a separate terminal (ensure port 80 isn't in use first):
docker run --rm --name littlelemon-caddy -p 80:80 caddy:alpine

then you should see something like this:
(venv) ubuntushyam@Shyam-MSI:~/projects/LittleLemon$ docker run --rm --name littlelemon-caddy -p 80:80 caddy:alpine
Unable to find image 'caddy:alpine' locally
alpine: Pulling from library/caddy
b8a5ec399796: Pull complete
4f4fb700ef54: Pull complete
6fd3ccaa8d5e: Pull complete
9c63ec053486: Pull complete
0a9a5dfd008f: Pull complete
Digest: sha256:b4e3952384eb9524a887633ce65c752dd7c71314d2c2acf98cd5c715aaa534f0
Status: Downloaded newer image for caddy:alpine
{"level":"info","ts":1744654169.0878937,"msg":"using config from file","file":"/etc/caddy/Caddyfile"}
{"level":"info","ts":1744654169.0890312,"msg":"adapted config to JSON","adapter":"caddyfile"}
{"level":"info","ts":1744654169.0908926,"logger":"admin","msg":"admin endpoint started","address":"localhost:2019","enforce_origin":false,"origins":["//localhost:2019","//[::1]:2019","//127.0.0.1:2019"]}
{"level":"warn","ts":1744654169.0911126,"logger":"http.auto_https","msg":"server is listening only on the HTTP port, so no automatic HTTPS will be applied to this server","server_name":"srv0","http_port":80}
{"level":"info","ts":1744654169.0915282,"logger":"tls.cache.maintenance","msg":"started background certificate maintenance","cache":"0xc000133700"}
{"level":"warn","ts":1744654169.0923061,"logger":"http","msg":"HTTP/2 skipped because it requires TLS","network":"tcp","addr":":80"}
{"level":"warn","ts":1744654169.0923574,"logger":"http","msg":"HTTP/3 skipped because it requires TLS","network":"tcp","addr":":80"}
{"level":"info","ts":1744654169.092366,"logger":"http.log","msg":"server running","name":"srv0","protocols":["h1","h2","h3"]}
{"level":"info","ts":1744654169.0947535,"msg":"autosaved config (load with --resume flag)","file":"/config/caddy/autosave.json"}
{"level":"info","ts":1744654169.094826,"msg":"serving initial configuration"}
{"level":"info","ts":1744654169.0985816,"logger":"tls","msg":"cleaning storage unit","storage":"FileStorage:/data/caddy"}
{"level":"info","ts":1744654169.1058028,"logger":"tls","msg":"finished cleaning storage units"}


Now, With the container running, visit http://localhost in your browser. You'll see Caddy page

Now return to your terminal, and exit the Caddy container by pressing Ctrl-C, then create a Caddyfile at your project root using VS code:
code Caddyfile

Configure it as follows: - from Source

http://localhost {
    # Serve static files from staticfiles directory
    handle /static/* {
        root * /srv/
        file_server
    }

    # Proxy all other requests to Gunicorn
    handle {
        reverse_proxy http://localhost:8000
    }
}

Corrected Caddyfile: from ChatGPT
http://localhost {
    # Serve static files from staticfiles directory
    handle /static/* {
        root * /srv/static
        file_server
    }

    # Proxy all other requests to Gunicorn
    handle {
        reverse_proxy http://localhost:8000
    }
}


# launch Caddy with Docker

Now launch Caddy with Docker, mounting both your static files and Caddy configuration:

docker run \
    --rm \
    --name littlelemon-caddy \
    -v $(pwd)/staticfiles:/srv/static \
    -v $(pwd)/Caddyfile:/etc/caddy/Caddyfile \
    --network host \
    caddy:alpine
	
or
	
docker run \
    --rm \
    --name littlelemon-caddy \
    -v $(pwd)/staticfiles:/srv/static \
    -v $(pwd)/Caddyfile:/etc/caddy/Caddyfile \
	--network host \
    -p 80:80 \
    caddy:alpine


# Optional: Run Gunicorn in background with logging

gunicorn Littlelemon.wsgi:application --bind 0.0.0.0:8000 --access-logfile gunicorn-access.log --error-logfile gunicorn-error.log --daemon


# Creating Dockerfile for Django apps

create an entrypoint.prod.sh script at your project root to handle database migrations, static files, and start Gunicorn:
#entrypoint.prod.sh
#!/usr/bin/env bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 django_project.wsgi:application

Next, create a Dockerfile in your project root with these instructions:

#Dockerfile
# Base image: Python 3.13 slim version for a minimal footprint
FROM python:3.13-slim AS builder

# Set working directory for all subsequent commands
WORKDIR /app

# Python environment variables:
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Upgrade pip to latest version
RUN pip install --upgrade pip

# Install system dependencies:
# libpq-dev: Required for psycopg2 (PostgreSQL adapter)
# gcc: Required for compiling some Python packages
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .
# Install Python dependencies without storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code to container
COPY . .

# Document that the container listens on port 8000
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x  /app/entrypoint.prod.sh

# Set the entrypoint script as the default command
# This will run migrations, collect static files, and start Gunicorn
CMD ["/app/entrypoint.prod.sh"]

# Building the Docker image

With the Dockerfile created, you'll now build a Docker image for your Django application. First, you'll set up a .dockerignore file to exclude unnecessary or sensitive files, then build and verify the image.

code .dockerignore

# .dockerignore

# See: https://gist.github.com/KernelA/04b4d7691f28e264f72e76cfd724d448
# Git
.git
.gitignore
.gitattributes


This file prevents sensitive data like environment variables from being included in your Docker image, similar to how .gitignore works for Git.
Now, go ahead and execute the command below to build the image:


docker build -t littlelemon-app .

Once the image is built successfully, you should see the following output:
[+] Building 245.1s (11/11) FINISHED

# Verify Docker Image
docker image ls littlelemon-app

# You should see the newly built image in the output:
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
littlelemon-app   latest    ec5473859174   24 minutes ago   502MB

Now that you have successfully built your Django application image, the next step will focus on launching your Django app alongside its Caddy and PostgreSQL dependencies through Docker Compose.

# Deploying the Django application with Docker Compose

Create a compose.yaml file in your project root:
code compose.yaml

Then paste in the following contents:

services:
  db:
    image: postgres:bookworm
    container_name: django-todo-db
    environment:
      - POSTGRES_DB=${DATABASE_NAME}
      - POSTGRES_USER=${DATABASE_USER}
      - POSTGRES_PASSWORD=${DATABASE_PASSWORD}
    env_file:
      - ./.env
    ports:
      - '5432:5432'
    volumes:
      - pg_data:/var/lib/postgresql/data

  web:
    build: .
    container_name: django-todo-app
    ports:
      - '8000:8000'
    environment:
      - DJANGO_DEBUG=${DJANGO_DEBUG}
      - DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
      - DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
      - DJANGO_CSRF_TRUSTED_ORIGINS=${DJANGO_CSRF_TRUSTED_ORIGINS}
      - DATABASE_ENGINE=${DATABASE_ENGINE}
      - DATABASE_NAME=${DATABASE_NAME}
      - DATABASE_USER=${DATABASE_USER}
      - DATABASE_PASSWORD=${DATABASE_PASSWORD}
      - DATABASE_HOST=${DATABASE_HOST}
      - DATABASE_PORT=${DATABASE_PORT}
    env_file:
      - ./.env
    depends_on:
      - db

  caddy:
    image: caddy:alpine
    container_name: django-todo-caddy
    ports:
      - 80:80
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./staticfiles:/srv/static
    depends_on:
      - web

volumes:
  pg_data:

This configuration:

Sets up PostgreSQL with persistent storage and health checks
Builds and runs your Django application with environment variables
Configures Caddy to serve static files and proxy requests to Django
Establishes proper service dependencies and networking

Before you launch the Docker compose stack, modify your Caddyfile and .env.local as follows:

# Caddyfile

http://localhost {
    # Serve static files from staticfiles directory
    handle /static/* {
        root * /srv/
        file_server
    }

    # Proxy all other requests to Gunicorn
    handle {
        reverse_proxy http://littlelemon-app:8000
    }
}


# .env

DJANGO_DEBUG=True
DJANGO_SECRET_KEY=django-insecure-@mvbih#nvlz%xs1thyud*#mlm97p+0g1mr)&6g_)c0$-os!rxz
DJANGO_ALLOWED_HOSTS=localhost
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=littlelemon-db
DATABASE_USER=postgres
DATABASE_PASSWORD=admin
# as per db service name in Docker compose file
DATABASE_HOST=db
DATABASE_PORT=5433

These changes ensure that the application components can communicate properly within the Docker network.

# Launch Application

The next step is to launch the stack with:
docker compose up

It will bring the containers up and you should see a bunch of logs from each container in your terminal:
[+] Running 4/4
 ✔ Network django-todo-app_default  Created                      0.2s
 ✔ Container django-todo-db         Created                      0.1s
 ✔ Container django-todo-app        Created                      0.1s
 ✔ Container django-todo-caddy      Created                      0.1s
Attaching to django-todo-app, django-todo-caddy, django-todo-db
. . .
django-todo-db     | 2025-02-10 11:12:20.747 UTC [29] LOG:  redo done at 0/1912180 system usage: CPU: user: 0.00 s, system: 0.00 s, elapsed: 0.00 s
django-todo-db     | 2025-02-10 11:12:20.759 UTC [27] LOG:  checkpoint starting: end-of-recovery immediate wait
django-todo-db     | 2025-02-10 11:12:20.843 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.026 s, total=0.096
s; sync files=2, longest=0.013 s, average=0.013 s; distance=0 kB, estimate=0 kB; lsn=0/19121B8, redo lsn=0/19121B8
django-todo-db     | 2025-02-10 11:12:20.852 UTC [1] LOG:  database system is ready to accept connections
django-todo-caddy  | {"level":"info","ts":1739185941.3228838,"msg":"using config from file","file":"/etc/caddy/Caddyfile"}
. . .
django-todo-caddy  | {"level":"info","ts":1739185941.344128,"msg":"serving initial configuration"}
django-todo-caddy  | {"level":"info","ts":1739185941.3572319,"logger":"tls","msg":"cleaning storage unit","storage":"FileStorage:/data/caddy"}
django-todo-caddy  | {"level":"info","ts":1739185941.3574784,"logger":"tls","msg":"finished cleaning storage units"}
django-todo-app    | Operations to perform:
django-todo-app    |   Apply all migrations: admin, auth, contenttypes, sessions, todo_app
django-todo-app    | Running migrations:
. . .
django-todo-app    | 127 static files copied to '/app/staticfiles', 1 unmodified.
django-todo-app    | [2025-02-10 11:12:23 +0000] [9] [INFO] Starting gunicorn 23.0.0
django-todo-app    | [2025-02-10 11:12:23 +0000] [9] [INFO] Listening at: http://0.0.0.0:8000 (9)
django-todo-app    | [2025-02-10 11:12:23 +0000] [9] [INFO] Using worker: sync
django-todo-app    | [2025-02-10 11:12:23 +0000] [10] [INFO] Booting worker with pid: 10
django-todo-app    | [2025-02-10 11:12:23 +0000] [11] [INFO] Booting worker with pid: 11
django-todo-app    | [2025-02-10 11:12:23 +0000] [12] [INFO] Booting worker with pid: 12
django-todo-app    | [2025-02-10 11:12:23 +0000] [13] [INFO] Booting worker with pid: 13


# Verify Application
To confirm that everything works, visit http://localhost in your browser. You should be able to interact with the application in the same way as before:

====================================================
# In case of any issues, fix it and Rebuild & run cleanly
docker compose down -v  # stop + remove volumes
docker compose build    # rebuild containers with new env
docker compose up       # run
====================================================

#  To double check .env exists inside container:

docker exec -it littlelemon-app env | grep DJANGO_SECRET_KEY

# Quick Check: What’s in your image?
docker run -it littlelemon-app sh

then explore with
ls -la



===========================================================================================================================

# Final Working Configuration

# Caddyfile
http://localhost {

	# Serve static files from ./staticfiles/
	handle_path /static/* {
		root * /srv/static
		file_server
	}

	# Proxy all other requests to Django via Gunicorn
	handle {
		reverse_proxy http://littlelemon-app:8000
	}
}

*****************************************************************************************************************************
# .env

# Django
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=django-insecure-@mvbih#nvlz%xs1thyud*#mlm97p+0g1mr)&6g_)c0$-os!rxz
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

# Database
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=littlelemon-db
DATABASE_USER=postgres
DATABASE_PASSWORD=admin
DATABASE_HOST=db
DATABASE_PORT=5432


*****************************************************************************************************************************
# .dockerignore
	# see https://gist.github.com/KernelA/04b4d7691f28e264f72e76cfd724d448

# Git and VCS
.git
.gitattributes
.github
.gitignore

# Django and Python
*.log
*.sqlite3
*.db
*.py[cod]
__pycache__/
*.pycache*/


# Documentation
!README.md
LICENCE
docs/
*.md  # optionally keep this if you only want README.md

# Scripts (exclude if only used locally)
update_readme.py
update_test_results.py

# Env/venv
.env/
*.env
.env.*
venv/
env/
pipfile
pipfile.lock

# Build/Test/Packaging
build/
dist/
*.egg-info/
.coverage
coverage.xml
htmlcov/
.mypy_cache/
.pytest_cache/
tests/
*/tests/
.mypy_cache/
.pytest_cache/

# Static/media (if you collect them externally)
staticfiles/
media/

# Docker
Dockerfile~
docker-compose.yml~
.docker

# OS/IDE
.DS_Store
Thumbs.db
.vscode/
.idea/
*.swp
*.swo

# Logs and database
*.log
*.sqlite3
*.db

# Node/npm junk (if any)
node_modules/
npm-debug.log
yarn-error.log


# Frontend artifacts
*.map
*.cache


# Migrations (optional — only if you auto-generate them)
# **DON'T** ignore if you're tracking migrations in VCS
# **Uncomment if needed**
# */migrations/
	
*****************************************************************************************************************************
# entrypoint.prod.sh

#!/usr/bin/env bash
set -e  # Exit on any error

echo "Running Django migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn Littlelemon.wsgi:application --bind 0.0.0.0:8000 --workers 3


*****************************************************************************************************************************
# Dockerfile

# ---------- STAGE 1: Builder ----------

# Base image: Python 3.13 slim version for a minimal footprint
FROM python:3.13-slim AS builder

# Set working directory for all subsequent commands
WORKDIR /app

# Python environment variables:
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Install system dependencies:
# libpq-dev: Required for psycopg2 (PostgreSQL adapter)
# gcc: Required for compiling some Python packages
# Upgrade pip to latest version
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .
# Install Python dependencies without storing pip cache
RUN pip install --user --no-cache-dir -r requirements.txt

# ---------- STAGE 2: Final image ----------
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
WORKDIR /app
    
# Add only necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    
# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
    
# Copy only needed files
COPY . .

# Document that the container listens on port 8000
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x  /app/entrypoint.prod.sh

# Set the entrypoint script as the default command
# This will run migrations, collect static files, and start Gunicorn
CMD ["/app/entrypoint.prod.sh"]

# -----------Health Check------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD curl --fail http://localhost:8000/health/ || exit 1


*****************************************************************************************************************************
# Readme
# Let's examine the key components of this Dockerfile:

#     The FROM instruction selects a minimal Python base image that includes only essential components needed to run Python applications.
    
#     WORKDIR /app establishes the working directory inside the container where all subsequent commands will execute.
    
#     The environment variables set by ENV statements optimize Python's behavior in containers:
    
#     PYTHONDONTWRITEBYTECODE=1 prevents Python from creating .pyc files
#     PYTHONUNBUFFERED=1 ensures Python output is sent directly to the terminal without buffering.
#     RUN pip install --upgrade pip ensures we have the latest version of pip for package installation.
    
#     The system dependencies installation combines two commands to minimize layers. Here, libpq-dev is required for PostgreSQL support through psycopg2, while gcc is needed to compile certain Python packages.
    
#     COPY requirements.txt . copies just the requirements file first, allowing Docker to cache the dependency installation layer.
    
#     RUN pip install --no-cache-dir -r requirements.txt installs all Python dependencies without storing pip's cache.
    
#     COPY . . copies all remaining application code into the container after dependencies are installed.
    
#     EXPOSE 8000 documents that the container listens on port 8000, though this is primarily for documentation purposes.
    
#     Finally, RUN chmod +x /app/entrypoint.prod.sh makes the entrypoint script executable, and CMD ["/app/entrypoint.prod.sh"] sets it as the default command when the container starts.
    
#     With the Dockerfile complete, you're ready to build your Docker image in the next step.

