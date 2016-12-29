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
          $scope.submitStudnetForm = function () {

              var onSuccess = function (data, status, headers, config) {
                  alert('Student saved successfully.');
                  $scope.formStudent = false;
                  $scope.initFirst();
              };

              var onError = function (data, status, headers, config) {
                  alert('Error occured.');
              }

              $http.post('/api/students.json/', { student:$scope.student })
                  .success(onSuccess)
                  .error(onError);

          };
          
          //create resetForm() function. This will be called on Reset button click.  
          $scope.resetForm = function () {
              $scope.student = angular.copy($scope.OriginalStudent);
          };
          
          $scope.deleteStudentForm = function (student_id) {

              var onSuccess = function (data, status, headers, config) {
                  alert('Student delete successfully.');
                  $scope.initFirst();
              };

              var onError = function (data, status, headers, config) {
                  alert('Error occured.');
              }

              $http.delete('/api/student.json/'+student_id)
                  .success(onSuccess)
                  .error(onError);
          };
          
          $scope.initFirst=function(){
        	  $http.get('/api/students.json/').success(function(data) {
      		    $scope.students = data.students;
      		  });
          };
          
          $scope.addNewStudent = function(){
        	  $scope.formStudent = true;
          };
//          $scope.updateStudentForm = function(student){
////        	  $scope.edit_id = student.id;
//        	  var onSuccess = function (data, status, headers, config) {
//                  alert('Student saved successfully.');
//                  $scope.formStudent = false;
//                  $scope.initFirst();
//              };
//
//              var onError = function (data, status, headers, config) {
//                  alert('Error occured.');
//              }
//
//              $http.put('/api/student.json/'+student.id, { student:$scope.student })
//                  .success(onSuccess)
//                  .error(onError);
//          };
	}]);

