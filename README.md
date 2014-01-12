Fuel-OD
==

[![Build Status](https://travis-ci.org/mchiodo/Fuel-OD.png?branch=master)](https://travis-ci.org/mchiodo/Fuel-OD)
[![Built with Grunt](https://cdn.gruntjs.com/builtwith.png)](http://gruntjs.com/)
This is the MVP for a open data project that will display -> "Fuel economy data are the result of vehicle testing done at the Environmental Protection Agency's National Vehicle and Fuel Emissions Laboratory in Ann Arbor, Michigan, and by vehicle manufacturers with oversight by EPA". 

You can find the data set at [fueleconomy.gov](http://www.fueleconomy.gov/feg/download.shtml). I personaly decided to only query data from 2011-2014, however this can be fixed via dataset variable in api.py.

I am currenly hosting it at my [personal subdomain](http://fuel.jarenglover.com). 

This project was great at teaching what it takes to host a web app. This included a stack from the OS up to REST API. 

Services:
--
 - Year
 - Make
 - All Car Data
 - YourSaveSpend
 - HighwayMPG
 - CityMPG

Installation Instructions
--
Fuel-OD requires Node.js, Django and a PostgresQL database.
### Node Setup:
#### Install Node.js dependencies and Bower
```
$ npm install
# npm install -g bower
```

### Django Setup:
#### Install Django dependencies and export settings
```
# pip install -r requirement_file.txt
$ export DJANGO_SETTINGS_MODULE='opendata.settings'
```

### Database Setup
```
$ vi opendata/settings.py
```
#### Add security key
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
```
#### Add local PostgresQL info
```
DATABASES = {
'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': '',
  'USER': '',
  'PASSWORD': '',
  'HOST': '',
  'PORT': '',
  }
}

```

#### Sync local DB with fueleconomy.gov database
```
$ python manage.py syncdb
$ python manage.py shell <parseCSV.py
```

Start Fuel-OD
--
```
$ python manage.py runserver 0.0.0.0:8732
```

#### Contributors: 
```
Back End OG -->Jaren Glover - @GloveDotcom - www.JarenGlover.com
Front End Capo -> Dan Carter - @dcarter_js
``` 

