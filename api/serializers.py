'''
Created on Dec 26, 2016

@author: realwat
'''
from rest_framework.serializers import HyperlinkedModelSerializer
from StudentList.models import Student
class StudentSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model=Student
        fields=("id","name","gender","birthday","register_date")
        