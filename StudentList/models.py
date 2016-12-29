from django.db import models
class Student(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    birthday = models.DateField()
    register_date = models.DateField()
    class Meta:
            ordering = ('name',)