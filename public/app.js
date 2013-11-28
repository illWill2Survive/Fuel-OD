/**
* This file launches the routes, controllers, and templates
*/

define([
	'angular',
	'ngRoute',
	'js/controllers/homectrl'
], function(angular) {
<<<<<<< HEAD
	return angular.module('openDataApp', [
		'ngRoute',
		'homeCtrl'
		])
		.config(['$routeProvider', function($routeProvider) {
			$routeProvider
				.when('/', {controller: 'HomeController', templateUrl: '/templates/home.html'});
=======
	return angular.module('app', ['ngRoute', 'homeCtrl'])
		.config(['$routeProvider', function($routeProvider) {
			$routeProvider
				.when('/', {controller: 'HomeController', templateUrl: '/index.html'});
>>>>>>> 24d9ab91e7b0bc4a76deb4dc872926cba3583ac8
		}]);
});