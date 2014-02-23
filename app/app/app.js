require('angular/angular');
require('angular-route/angular-route');
require('./bootstrap');
var imagefact = require('./imagefact'),
    mainctrl = require('./mainctrl'),
    aboutctrl = require('./aboutctrl');


//Declare app level module and dependencies
angular.module('sampleApp', [
        'ngRoute'
    ])
    .config(['$routeProvider', function ($routeProvider) {
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

//Load factories
angular.module('sampleApp').factory('ImageFactory', imagefact.ImageFactory);

//Load controller(s)
angular.module('sampleApp').controller('MainCtrl', ['$scope', mainctrl.MainController]);
angular.module('sampleApp').controller('AboutCtrl', ['$scope', 'ImageFactory', aboutctrl.AboutController]);