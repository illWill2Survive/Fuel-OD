/**
* Home Controller: Used to load the home page.
*/

define([
	'angular'
], function(angular) {
	return angular.module('homeCtrl', [])
		.controller('HomeController', ['$scope', function ($scope) {
			$scope.test = 'controller finally loaded';
		}]);
});
