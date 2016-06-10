angular
    .module('videoVillage')
    .factory('Video', ['$resource', function($resource){
        return $resource('/api/videos/:videoId.json', {}, {
            query:{
                method: 'GET',
                // params: {videoId: 'videos'},
                isArray: true
            }
        })
}]);