#!/bin/bash

#Author Jaren
#Website www.jarenglover.com
#Contact @GloveDotcom

NAME="fuel_opendata"                            # Name of the application
DJANGODIR=`pwd`
SOCKFILE=${DJANGODIR}/run/gunicorn.conf  	    # we will communicte using this unix socket
USER=fuel                                       # the user to run as
GROUP=webapps                                   # the group to run as
NUM_WORKERS=3                                   # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=opendata.settings        # which settings file should Django use
DJANGO_WSGI_MODULE=opendata.wsgi                # WSGI module name
LOGFILE=${DJANGODIR}/log/fuel.log		        # location of log file
LOGDIR=$(dirname $LOGFILE)			            # location of log directory 
VIRENV=$DJANGODIR/../env			            # you have to have the virtual env in the same director as your django dir

echo "Starting $NAME as `whoami`"

#check if if used updated DB stuff
echo "Press 'Y' if you have updated your Database information, followed by \
[ENTER]" 

read command #take user input 

if [ ! "$command" = "Y" ] && [ ! "$command" = "y" ]; then
        echo "exiting! You need to update your DB info or follow directions!"
        exit 187   
fi 

#kill gunicorn if running 
if [[ ! -n $(ps cax | grep gunicorn) ]]; then
    pkill gunicorn || {echo "pkill failed" ; exit 1}

    echo " Just killed the current running gunicorn process" 
fi

# Activate the virtual environment
cd $DJANGODIR
source ${VIRENV}/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE #set the django model 
export PYTHONPATH=$DJANGODIR:$PYTHONPATH  		#add django dir to python path

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
test -d $LOGDIR || mkdir -p $LOGDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
echo "starting gunicorn for $NAME"

exec ${VIRENV}/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --log-level=debug \
  --log-file=$LOGFILE \
  --config=$SOCKFILE #2>> $LOGFILE 


#check if rebuild CSS and js
echo "Press 'Y' if you DONT want to rebuild CSS and JS, followed by \
[ENTER]" 

read command #take user input 

if [ ! "$command" = "Y" ] && [ ! "$command" = "y" ]; then
    grunt build  || {echo "grunt failed" ; exit 1}
         
fi 

#ask to clear redis cache 
echo "Press 'Y' if you want to clearn redis' cache, followed by \
[ENTER]" 

read command #take user input 

if [ ! "$command" = "Y" ] && [ ! "$command" = "y" ]; then
    redis-cli FLUSHALL || {echo "redis failed" ; exit 1}
fi

nohup node server.js || echo "ERRRRROR Couldn start node server" 

echo "script completed"
