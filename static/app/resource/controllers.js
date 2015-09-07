var angular = require('angular');

angular.module('example.api.controllers', [])
    .controller('ResourceController', ['$scope', 'postService', function ($scope, postService) {
        $scope.posts = {};
        postService.query(function (data) {
            $scope.posts = data;
        });
    }]);
