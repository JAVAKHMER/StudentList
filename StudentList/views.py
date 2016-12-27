from rest_framework.views import APIView
from StudentList.forms import StudentForm
from StudentList.models import Student
from django.shortcuts import render, redirect, get_object_or_404
class DisplayStudentView(APIView):
    def get(self,request):
        students = Student.objects.all()
        return render(request, 'student_list.html', {'students': students})

class insertStudentView(APIView):
    def get(self,request):
        form = StudentForm()
        return render(request, 'insert_student.html', {'form': form})
    def post(self,request):
        if request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        return render(request, 'insert_student.html', {'form': form})
class updateStudentView(APIView):
    def get(self,request,id_student):
        student = get_object_or_404(Student, id=id_student)
        form = StudentForm(request.POST or None, instance=student)
        return render(request, "insert_student.html", {'form': form})
                
    def post(self,request,id_student):
        student = get_object_or_404(Student, id=id_student)
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, "insert_student.html", {'form': form})
class deleteStudentView(APIView):
    def get(self,request,id_student):
        student = Student.objects.get(id=id_student)
        student.delete()
        return redirect('student_list')
#         students = Student.objects.all()
#         return render(request, 'student_list.html', {'students': students})

class HomePage(APIView):
    def get(self,request):
        return render(request,'index.html')
class InsertStudent(APIView):
    def get(self,request):
        return render(request,'insert.html')
class UpdateStudent(APIView):
    def get(self,request):
        return render(request,'insert.html')
       
    
    
    
    
    
    
    