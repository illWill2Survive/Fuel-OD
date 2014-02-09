#!/bin/bash

NAME="fuel_opendata"                                  # Name of the application
DJANGODIR=`pwd`
SOCKFILE=${DJANGODIR}/run/gunicorn.conf  	# we will communicte using this unix socket
USER=fuel                                        # the user to run as
GROUP=webapps                                    # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=opendata.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=opendata.wsgi                     # WSGI module name
LOGFILE=${DJANGODIR}/log/fuel.log		#location of log file
LOGDIR=$(dirname $LOGFILE)			#location of log directory 
VIRENV=$DJANGODIR/../env			#you have to have the virtual env in the same director as your django dir
API="tastypie"
#echo $VIRENV
#cd ${VIRENV}
#echo `pwd`
echo "Starting $NAME as `whoami`"

#check if if used updated DB stuff
echo "Press 'Y' if you have updated your Database information, followed by
[ENTER]" 
read answer 

    if [ ! "$command" == "Y" ] || [ ! "$command" == "y" ]; then
        exit 187   
    fi 
#kill gunicorn if running 
pkill gunicorn 

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
exec ${VIRENV}/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --log-level=debug \
  --log-file=$LOGFILE \
  --config=$SOCKFILE 2>> $LOGFILE  

'''if [ ! -d $API ]; then
    echo "Type \"Y\" to auto download Tastypie artifacts , followed by [ENTER]:"
    read command 

    if [ "$command" == "Y" ] || [ "$command" == "y" ]; then
        git clone https://github.com/toastdriven/django-tastypie
    fi 
fi
'''
