from rest_framework.views import APIView
from StudentList.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
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
        return Response(lserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAPIView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self,request,obj_id):
#         try:
#             student = Student.objects.get(obj_id)
#             lserializer = StudentSerializer(student, data=request.data, partial=True)
#             if lserializer.is_valid():
#                 lserializer.save()
#                 return Response(lserializer.data)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         
#     def delete(self,request,obj_id):
#         try:
#             student = Student.objects.get(obj_id)
#             student.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     
    
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
