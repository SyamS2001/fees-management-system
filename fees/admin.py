from typing import Any
from django.contrib import admin
from .models import*

class StateAdmin(admin.ModelAdmin):
    list_display=('statename','created_date','isactive')
    search_fields=('statename',)

admin.site.register(State, StateAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display=('Districtname','statename','created_date','isactive')
    exclude=['created_user']
    search_fields=('Districtname','statename_statename',)

admin.site.register(District, DistrictAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display=('Companyname','Districtname','phone_no','website','isactive','created_date')
    list_filter=('Districtname','isactive')

admin.site.register(Company, CompanyAdmin)

class QualificationAdmin(admin.ModelAdmin):
    list_display=('Qualificationname','isactive','created_date')

admin.site.register(Qualification,QualificationAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=('Coursename','coursecode','amount','duration','isactive')
    list_filter=('Coursename','isactive')

admin.site.register(Course, CourseAdmin)



