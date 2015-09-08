var angular = require('angular');
require('angular-resource');
// ngResource nos ayuda a consumir APIRest
var service = angular.module('example.api.services', ['ngResource']);

service.factory('postService', ['$resource', function ($resource) {
        return $resource('/api/v1/posts/:id');
    }]);
