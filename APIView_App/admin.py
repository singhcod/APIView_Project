from django.contrib import admin

# Register your models here.
from APIView_App.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','salary']
