/* Project specific Javascript goes here. */
var app = angular.module('videoVillage', ['ngResource']);

app.controller('VideoController', function VideoController($scope, Video){
    $scope.videos = Video.query();
});