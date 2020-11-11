from django.urls import path
from .views import CreateEmployeeView, DepartmentDetailView, DepartmentListView

urlpatterns = [
    path('create-employee/', CreateEmployeeView.as_view(), name='create-employee'),
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('department/<pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]