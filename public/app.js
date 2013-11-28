/**
* This file launches the routes, controllers, and templates
*/

define([
	'angular',
	'ngRoute',
	'js/controllers/homectrl'
], function(angular) {
	return angular.module('app', ['ngRoute', 'homeCtrl'])
		.config(['$routeProvider', function($routeProvider) {
			$routeProvider
				.when('/', {controller: 'HomeController', templateUrl: '/index.html'});
		}]);
});