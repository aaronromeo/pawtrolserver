#!/bin/bash
 
NAME="pawtrolserver"                                  # Name of the application
DJANGODIR=/data/venv_pawtrolserver/pawtrolserver/pawtrolserver/             # Django project directory
SOCKFILE=/data/tmp/pawtrolserver_gunicorn.sock  # we will communicte using this unix socket
USER=deploy                                        # the user to run as
GROUP=deploy                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=pawtrolserver.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=pawtrolserver.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source /data/venv_pawtrolserver/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

source /data/venv_pawtrolserver/pawtrolserver/serverdeploy/vars.secure

env

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /data/venv_pawtrolserver/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE
