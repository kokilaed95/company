# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length = 254)
    date_of_birth = models.DateField(null=True, blank=True)
    picture = models.ImageField(blank=True, null=True)
    department = models.ForeignKey(
        'Department', related_name='manager', null=True, blank=True, 
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    department_manager = models.ForeignKey(
    	Employee, related_name='manager', null=True, blank=True, 
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name