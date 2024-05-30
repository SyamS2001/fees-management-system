from django.contrib import admin
from.models import*

#Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=('studentname','companyname','statename','Districtname','Coursename','created_date','isactive')
    list_filter=('studentname','isactive')

admin.site.register(student, studentAdmin)

class receiptAdmin(admin.ModelAdmin):
    list_display=('receiptno','studentname','amount')
    list_filter=('receiptno','isactive')

admin.site.register(receipt, receiptAdmin)
