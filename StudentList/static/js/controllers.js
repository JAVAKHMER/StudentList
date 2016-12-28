var myApp = angular.module('myApp', []);
myApp.config(['$interpolateProvider','$httpProvider',
    function( $interpolateProvider,$httpProvider) {
	$interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
},
]);
    
myApp.controller('studentController', ['$scope', '$http', function($scope, $http) {
		  $http.get('/api/students.json/').success(function(data) {
		    $scope.students = data.students;
		  });
//          $scope.originalStudent = {
//              name: 'panha',
//              birthday: new Date('12/07/1994'),
//              register_date: new Date('12/27/2016'),
//              gender: 'M',
//          };
//
//          //copy originalStudent to student. student will be bind to a form 
//          $scope.student = angular.copy($scope.originalStudent);

          //create submitStudentForm() function. This will be called when user submits the form
          $scope.submitStudnetForm = function () {

              var onSuccess = function (data, status, headers, config) {
                  alert('Student saved successfully.');
              };

              var onError = function (data, status, headers, config) {
                  alert('Error occured.');
              }

              $http.post('/api/students.json/', { student:$scope.student })
                  .success(onSuccess)
                  .error(onError);

          };

          //6. create resetForm() function. This will be called on Reset button click.  
          $scope.resetForm = function () {
              $scope.student = angular.copy($scope.OriginalStudent);
          };
	}]);
//myApp.controller('MyController', function MyController($scope, $http) {
//	$http({
//        url: "/api/students.json/", 
//        method: "GET",
//	}).then(function(response){
//		$scope.students = response.data.students;
//	});
//});

