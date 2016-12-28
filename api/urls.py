
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^students.json/', views.StudentsAPIViews.as_view()),
    url(r'^student.json/(?P<pk>[0-9]+)/$', views.StudentAPIView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)