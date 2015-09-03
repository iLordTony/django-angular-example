/**
 * Created by Carlos Tonatihu on 01/09/2015.
 */
(function () {
    var angular = require('angular');
    var app = angular.module('example', []);

    app.controller('AppController', ['$scope', '$http', function ($scope, $http) {
        $scope.posts = [];
        $http.get('/api/v1/posts').then(function (results) {
            debugger;
            results.data.forEach(function (item) {
                $scope.posts.push(item);
            })
        });
    }]);
})();
