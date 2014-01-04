#!/bin/bash

NAME="fuel_opendata"                                  # Name of the application
DJANGODIR=/webapps/fuel_django/Fuel-OD/
SOCKFILE=/webapps/fuel_django/Fuel-OD/run/gunicorn.sock  # we will communicte using this unix socket
USER=fuel                                        # the user to run as
GROUP=webapps                                    # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=opendata.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=opendata.wsgi                     # WSGI module name
LOGFILE=/webapps/fuel_django/Fuel-OD/log/fuel.log
LOGDIR=$(dirname $LOGFILE)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
echo `pwd`
source ../Fuel-OD/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
test -d $LOGDIR || mkdir -p $LOGDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../Fuel-OD/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --log-level=debug \
  --log-file=$LOGFILE \
  --config=$SOCKFILE 2>> $LOGFILE  #bind=unix:$SOCKFILE
