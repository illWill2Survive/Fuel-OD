/**
* This file launches the routes, controllers, and templates
*/

define([
	'angular',
	'ngRoute',
	'./controllers/homectrl'
], function(angular) {
	return angular.module('openDataApp', [
		'ngRoute',
		'homeCtrl'
		])
		.config(['$routeProvider', function($routeProvider) {
			$routeProvider
				.when('/', {controller: 'HomeController', templateUrl: 'js/templates/home.html'});
		}]);
});