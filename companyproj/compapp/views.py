from django.shortcuts import render, redirect
from .models import Employee, Project
from django.utils import timezone

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today, 
                                        end_date__gte=today  )
    
    #projects = employee.projects.all()
    return render(request, 'employee_detail.html', 
                  {'employee': employee, 'projects': projects})

def employee_engineers(request):
    employees = Employee.objects.filter(position__icontains="engineer")
    return render(request, 'employee_list.html', {'employees': employees})



#forms

#from .forms import PostForm #2

#def create_post(request):
  #form = PostForm(request.POST or None) #3

  #data = {}
  #data["form"] = form #4

  #if form.is_valid(): #5
    post = form.save() #6
    return redirect("show-post", s=post.slug) #7

  #return render(request, 'create_post.html', data) #8


from .forms import EmployeeForm, ProjectForm

def create_employee(request):
    form = EmployeeForm(request.POST or None)

    data = {"form": form}

    if form.is_valid():
        form.save()
        return redirect("employee_list")   # ← your list page

    return render(request, "add_employee.html", data)


def create_project(request):
    form = ProjectForm(request.POST or None)

    data = {"form": form}

    if form.is_valid():
        form.save()
        return redirect("employee_list")   # redirect to employee list page

    return render(request, "project.html", data)



