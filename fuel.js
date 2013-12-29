var express = require('express'),
mustache = require('mustache'),
path = require('path');

var app = express();


var DEBUG = true;

app.configure(function(){
	app.set('port', 8080);
	app.set('view engine', 'mustache');
	app.use(express.logger());
	app.use(express.bodyParser());
	app.use(express.methodOverride());
	app.use(app.router);
	//TODO handle environment configurations better
	if(DEBUG){
		console.log('Using local configuration');
		app.use(express.static(path.join(__dirname, 'public')));
		console.log('Fuel-OD app module loaded in local configuration');
	} else {
		app.use(express.static(path.join(__dirname, 'dist')));
	}
	
});

module.exports = app;
