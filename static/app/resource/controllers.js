var angular = require('angular');

angular.module('example.api.controllers', [])
    .controller('ResourceController', ['$scope', 'postService', function ($scope, postService) {
        $scope.posts = {};
        // Se usa query porque se va a recivir un arreglo, de lo contrario se usa get
        postService.query(function (data) {
            $scope.posts = data;
        });
    }]);
