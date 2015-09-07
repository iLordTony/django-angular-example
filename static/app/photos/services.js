var angular = require('angular');
require('angular-resource');

var services = angular.module('example.photos.services', ['ngResource']);

services.factory('userPostService', ['$resource', function ($resource) {
    return $resource('/api/v1/:username/posts/:id');
}]);

services.factory('postPhotoService', ['$resource', function ($resource) {
    return $resource('/api/v1/posts/:post_id/photos/:id');
}]);
