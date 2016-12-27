from rest_framework.views import APIView
from StudentList.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
class StudentsAPIViews(APIView):
    
    def get(self, request):
        lret_dict = dict()
        try:
            lstudents = Student.objects.all()
            lserializer = StudentSerializer(lstudents, many=True)
            lret_dict = dict(students=lserializer.data)
        except Exception, err:
            print(err)
            pass   
        return Response(lret_dict, status=status.HTTP_200_OK)
    
    def post(self, request):
        lserializer = StudentSerializer(data=request.DATA.get('student'))
        if lserializer.is_valid():
            lserializer.save()
            return Response(lserializer.data, status=status.HTTP_201_CREATED)
        else:
            print lserializer.errors
        return Response(lserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAPIView(APIView):
    
    def put(self,request,obj_id):
        try:
            student = Student.objects.get(obj_id)
            lserializer = StudentSerializer(student, data=request.data)
            if lserializer.is_valid():
                lserializer.save()
                return Response(lserializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,obj_id):
        try:
            student = Student.objects.get(obj_id)
            student.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#     def put(self, request, obj_id):
#         student = self.get_object(obj_id)
#         serializer = StudentSerializer(student, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     
#     def delete(self, request, obj_id):
#         student = self.get_object(obj_id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
