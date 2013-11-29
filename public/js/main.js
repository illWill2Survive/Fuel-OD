/**
* Require JS configuration.  Defines and launches the main app.
*/

require.config({
	baseUrl: '/',
	paths: {
		'domReady' : '../bower_components/requirejs-domready/domReady',
        'text' : '../bower_components/requirejs-text/requirejs-text',
		'angular' : '../bower_components/angular/angular',
		'ngRoute' : '../bower_components/angular-route/angular-route'
	},
	shim: {
		'angular' : { exports : 'angular'},
		'ngRoute' : { deps:['angular']} 
	},
	priority: [
		'angular'
	]
});

require([
	'domReady',
	'angular',
	'js/app'
], (function(domReady, angular, app) {
	domReady(function() {
		console.log('dom is ready');
		angular.bootstrap(document, ['openDataApp']);
		console.log('application is bootstrapped');
	});
}));
