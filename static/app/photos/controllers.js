var angular = require('angular');
angular.module('example.photos.controllers', ['example.api.services'])
    .controller('PhotosController', ['$scope', 'postService', 'postPhotoService', function ($scope, postService, postPhotoService) {
        $scope.photos = {};
        $scope.posts = postService.query();
        $scope.posts.$promise.then(function (data) {
            angular.forEach(data, function (post) {
                postPhotoService.query({post_id: post.id}, function (data) {
                    $scope.photos[post.id] = data;
                    debugger;
                });
            });
        });

    }]);
