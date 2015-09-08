var angular = require('angular');

angular.module('example.photos.controllers', ['example.api.services'])
    .controller('PhotosController', ['$scope', 'postService', 'postPhotoService', function ($scope, postService, postPhotoService) {
        $scope.photos = {};
        $scope.posts = postService.query(); // Obtiene todos los posts
        $scope.posts.$promise.then(function (results) {
            // Esto se realiza por cada post
            results.forEach(function (post) {
                // Esto obtendra todas las fotos por cada post
                postPhotoService.query({post_id: post.id}, function (data) {
                    $scope.photos[post.id] = data;
                });
            });
        });
    }]);
