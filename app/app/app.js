require('angular/angular');
require('angular-route/angular-route');
require('./bootstrap');
var mainctrl = require('./mainctrl');
var aboutctrl = require('./aboutctrl');

//Declare app level module and dependencies
angular.module('sampleApp', [
    'ngRoute'
    ])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/app/templates/home.html', 
                controller: 'MainCtrl'
            })
            .when('/about'), {
                 templateUrl: '/app/templates/about.html',
                 controller:'AboutCtrl'
            }
            .otherwise( 
                {
                    redirectTo: '/'
                });
    }]);

//Load controller(s)
angular.module('sampleApp').controller('MainCtrl', ['$scope', mainctrl.MainController]);    
angular.module('sampleApp').controller('AboutCtrl', ['$scope', aboutctrl.AboutController]);
