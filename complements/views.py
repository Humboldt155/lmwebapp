from django.shortcuts import render
from .models import Department, \
                    SubDepartment, \
                    Attribute, \
                    Value, \
                    DepartmentAdeo, \
                    SubDepartmentAdeo, \
                    ModelGroupAdeo, \
                    LMCode, \
                    Document

# Create your views here.

def index(request):

    return render(request, 'index.html')