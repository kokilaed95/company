from django.contrib import admin
from .models import Department, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_filter = ('department',)
    date_hierarchy = 'date_of_birth'

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline,]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
