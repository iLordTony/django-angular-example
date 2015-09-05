var angular = require('angular');
angular.module('example.basic.services', [])
.factory('basicService', ['$http', '$q', function ($http, $q) {

    function get_posts() {
        var deffered = $q.defer();
        $http.get('/api/v1/posts').success(function (data) {
            deffered.resolve(data);
        })

        return deffered.promise;
    }

    return {
        get_posts: get_posts
    };
}]);
