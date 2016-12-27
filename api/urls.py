
from django.conf.urls import include, url
from api import views
urlpatterns = [
    url(r'^students.json/', views.StudentsAPIViews.as_view()),
    url(r'^student.json/', views.StudentAPIView.as_view()),
#     url(r'^students/(\d+).json/', views.StudentAPIViews.as_view())
]
