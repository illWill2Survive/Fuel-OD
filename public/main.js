/**
* Require JS configuration.  Defines and launches the main app.
*/

require.config({
	baseUrl: '/',
	paths: {
		'domReady' : '/bower_components/requirejs-domready/domReady',
		'angular' : '/bower_components/angular/angular',
		'ngRoute' : '/bower_components/angular-route/angular-route'
	},
	shim: {
		'angular' : { exports : 'angular'},
		'ngRoute' : { deps:['angular']} 
<<<<<<< HEAD
	},
	priority: [
		'angular'
	]
=======
	}
>>>>>>> 24d9ab91e7b0bc4a76deb4dc872926cba3583ac8
});

require([
	'domReady',
	'angular',
	'app'
], (function(domReady, angular, app) {
	domReady(function() {
<<<<<<< HEAD
		console.log('dom is ready');
		angular.bootstrap(document, ['openDataApp']);
		console.log('application is bootstrapped');
	});
=======
	console.log('dom is ready');
	angular.bootstrap(document, ['app']);
	console.log('application is bootstrapped');
	});

>>>>>>> 24d9ab91e7b0bc4a76deb4dc872926cba3583ac8
}));