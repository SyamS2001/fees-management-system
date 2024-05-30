from django.db import models
from django.contrib.auth.models import User

class Master(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    isactive=models.BooleanField(default=True,verbose_name="Active")
    created_user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class State(Master):
    statename=models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural='States'

    def __str__(self):
        return self.statename
    
class District(Master):
    statename=models.ForeignKey(State, on_delete=models.CASCADE, limit_choices_to={'isactive': True})
    Districtname=models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural='Districts'

    def __str__(self):
        return self.Districtname
    
class Company (Master):
    Districtname= models.ForeignKey(District, on_delete=models.CASCADE)
    Companyname= models.CharField(max_length=200)
    address= models.TextField(max_length=1000)
    phone_no= models.CharField(max_length=10)
    website= models.URLField(max_length=100)

    class Meta:
        verbose_name_plural='Company'

    def __str__(self):
        return self.Companyname
    
class Qualification(Master):
    Qualificationname=models.CharField(max_length=200)

    class meta:
        verbose_name_plural='Qualification'

    def __str__(self):
        return self.Qualificationname
    
class Course(Master):
    Coursename=models.CharField(max_length=100)
    coursecode=models.CharField(max_length=15)
    amount=models.CharField(max_length=10)
    duration=models.CharField(max_length=100)

    class meta:
        verbose_name_plural='Course'

    def __str__(self):
        return self.Coursename
