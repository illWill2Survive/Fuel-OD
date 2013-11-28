define([
	'angular',
	'ngRoute'
], function(angular) {
	return angular.module('app', ['ngRoute'])
		.config(['$routeProvider', function($routeProvider) {
			$routeProvider
				.when('/', {controller: 'CHANGEME', templateUrl: '/CHANGEME'});
		}]);
});