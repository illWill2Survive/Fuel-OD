require('angular/angular');
require('angular-route/angular-route');
require('./bootstrap');
var mainctrl = require('./mainctrl'),
    aboutctrl = require('./aboutctrl');

//Declare app level module and dependencies
angular.module('sampleApp', [
    'ngRoute'
    ])
    .config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
       $locationProvider.html5Mode(true);
        $routeProvider
            .when('/', {
                templateUrl: '/app/templates/home.html', 
                controller: 'MainCtrl'
            })
            .when('/about', {
                 templateUrl: '/app/templates/about.html',
                 controller: 'AboutCtrl'
            })
            .otherwise(
                {
                    redirectTo: '/'
                });
    }]);

//Load controller(s)
angular.module('sampleApp').controller('MainCtrl', ['$scope', mainctrl.MainController]);    
angular.module('sampleApp').controller('AboutCtrl', ['$scope', aboutctrl.AboutController]);
