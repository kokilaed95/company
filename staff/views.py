from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import EmployeeForm
from .models import Department, Employee


class CreateEmployeeView(CreateView):
    
    form_class = EmployeeForm
    success_url = '/staff/departments/'
    template_name = 'staff/create_employee.html'


class DepartmentListView(ListView):

    model = Department


class DepartmentDetailView(DetailView):

    model = Department

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(**kwargs)
        employees = []
        if kwargs.get('object'):
            employees = Employee.objects.filter(department=kwargs.get('object'))
        context['employees'] = employees
        return context
