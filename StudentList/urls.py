
from django.conf.urls import include, url
from django.contrib import admin
from StudentList.views import DisplayStudentView, updateStudentView, deleteStudentView,\
    insertStudentView, HomePage, InsertStudent, UpdateStudent
from django.shortcuts import render

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^student/$', DisplayStudentView.as_view(),name='student_list'),
#     url(r'^updateStudent/(\d+)/$', updateStudentView.as_view(),name='update_student'),
#     url(r'^deleteStudent/(\d+)/$', deleteStudentView.as_view(),name='delete_student'),
#     url(r'^insertStudent/$', insertStudentView.as_view(),name='insert_student'),
    url(r'^$', HomePage.as_view(),name="home_page"),
    url(r'^insert$',InsertStudent.as_view(),name="insert"),
    url(r'^update/(\d+)$',UpdateStudent.as_view(),name="update"),
    url(r'^delete/(\d+)$',UpdateStudent.as_view(),name="delete"),
    url(r'^api/', include('api.urls')),
]
