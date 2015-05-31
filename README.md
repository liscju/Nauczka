## Building Local

You need:
* Python
* Postgresql
* virtualenv
* pip
* foreman

Prepare the local environment for the app by:
(virtualenv should be in python dir)
* $ virtualenv venv

Now download dependencies of application by:
(in windows with .exe suffix)
$ venv/Scripts/pip install -r requirements.txt --allow-all-external

windows:
venv\Scripts\pip.exe install -r requirements.txt --allow-all-external

## Database
* Install postgresql(for windows 9.3 x32 for x64 there is
     some problems)
* Create user
* Create schema

In env. file declare:
* DATABASE_URL=postgres://{{user}}:{{password}}@localhost:5432/{{schema}}
* PYTHONUNBUFFERED=True ( for easier debugging)

If you have problem with connection check if in your
database dir ( Postgre\9.3\data\pg_hba.conf) you can
connect locally without encrypting:

# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust


## Run
foreman start web -f Procfile.dev