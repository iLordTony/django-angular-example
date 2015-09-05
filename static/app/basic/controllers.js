var angular = require('angular');
angular.module('example.basic.controllers', [])
.controller('BasicController', ['$scope', 'basicService', function ($scope, basicService) {
    basicService.get_posts().then(function (data) {
        $scope.posts = data;
    });
}]);
