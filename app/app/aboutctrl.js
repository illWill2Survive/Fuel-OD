require('angular/angular');

exports.AboutController = function($scope, ImageFactory) {
    $scope.images = ImageFactory.images;

    $scope.test = 'testing';
};