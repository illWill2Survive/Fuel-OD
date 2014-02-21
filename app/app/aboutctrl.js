require('angular/angular');
require('./imagefact');

exports.AboutController = function($scope, ImageFactory) {
    $scope.whatsupdoc = "This app is dope";
    console.log(ImageFactory.images);
};