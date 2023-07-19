from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib import messages
from api.serializers import * 
from rest_framework.parsers import JSONParser
# Create your views here.
def index(request):
    
    
    context={

    }
    return render(request,'index.html',context)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})




def department(request):
    context ={}
    all_departments=Department.objects.all()
    # context['departmentform']= DepartmentForm()
    context={
        'departmentform':DepartmentForm(),
        'all_departments':all_departments,
    }
    if request.method == 'POST':
        form=DepartmentForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Department has been saved successfully')
            
        else:
            messages.error(request, 'Department cannot be saved') 
        
    return render(request, "department.html", context)

def department_delete(request,id):
    
    department=Department.objects.get(pk=id)
    department.delete()
    return redirect('/department')

def update_department(request, id):
    department = Department.objects.get(pk=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department has been updated successfully')
            return redirect('/department')
        else:
            messages.error(request, 'Department could not be updated')

    else:
        form = DepartmentForm(instance=department)

    context = {
        'form': form,
        'department': department
    }
    return render(request, 'update_department.html', context)






@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def department_detail(request, id):
    try:
        department = Department.objects.get(pk=id)
    except Department.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Department has been created successfully')
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Department has been updated successfully')
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        messages.success(request, 'Department has been deleted successfully')
        return Response(status=204)
