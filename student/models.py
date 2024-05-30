from django.db import models
from fees.models import*

# Create your models here.

class student(Master):
    studentname=models.CharField(max_length=100)
    companyname=models.ForeignKey(Company, on_delete=models.CASCADE)
    statename=models.ForeignKey(State,on_delete=models.CASCADE, limit_choices_to={'isactive': True})
    Districtname=models.ForeignKey(District, on_delete=models.CASCADE)
    Qualificationname=models.ForeignKey(Qualification, on_delete=models.CASCADE)
    Coursename=models.ForeignKey(Course, on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)

    class meta:
        verbose_name_plural='students'

    def __str__(self):
        return self.studentname
    
class receipt(Master):
    logo=models.ImageField(upload_to='uploads')
    receiptno=models.CharField(max_length=15)
    studentname=models.ForeignKey(student, on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)

    class meta:
        verbose_name_plural='Receipt'

    def __str__(self):
        return self.receiptno


