from django.shortcuts import render,redirect
from .models import EmployeeData
from django.http import HttpResponse
from django.db.models import Q
import faker
fake=faker.Faker()

def generateDate(request):
    for i in range(10):
        fname=fake.first_name()
        lname=fake.last_name()
        email=fake.email()
        loc=fake.random_element(elements=('hyd','bang','chennai','pune'))
        salary=fake.random_element(elements=(30000,10000,50000,40000))
        job=fake.random_element(elements=('admin','trainer','software','HR'))
        company=fake.random_element(elements=('TCS','WIPRO','CTS','INFOSYS'))
        address=fake.address()

        EmployeeData(
        first_name=fname,
        last_name=lname,
        email=email,
        location=loc,
        salary=salary,
        job=job,
        company=company,
        address=address
        ).save()
    return redirect('fetching_data')

def fetching_data(request):
    employee=EmployeeData.objects.all()
    context={'employee':employee}
    return render(request,'fetching_data.html',context)
def mainpage (request):
    return render(request,'mainpage.html')
def hyd_data(request):
    if request.method=="GET":
      hyd_data=EmployeeData.objects.filter(location='hyd')
      context={'hyd_data':hyd_data}
      return render(request,'hyd_data.html',context)
    else:
      cname=request.POST.get('cname')
      hyd_data=EmployeeData.objects.filter(Q(location='hyd') & Q(company=cname))
      context={'hyd_data':hyd_data}
      return render(request,'hyd_data.html',context)

def bang_data(request):
    if request.method=="GET":
     bang_data=EmployeeData.objects.filter(location='bang')
     context={'bang_data':bang_data}
     return render(request,'bang_data.html',context)
    else:
        cname=request.POST.get('cname')
        bang_data=EmployeeData.objects.filter(Q(location='bang') & Q(company=cname))
        context={'bang_data':bang_data}
        return render(request,'bang_data.html',context)

def chennai_data (request):
    if request.method=="GET":
      chennai_data=EmployeeData.objects.filter(location='chennai')
      context={'chennai_data':chennai_data}
      return render(request,'chennai_data.html',context)
    else:
      cname=request.POST.get('cname')
      chennai_data=EmployeeData.objects.filter(Q(location='chennai') & Q(company=cname))
      context={'chennai_data':chennai_data}
      return render(request,'chennai_data.html',context)

def pune_data(request):
    if request.method=="GET":
     pune_data=EmployeeData.objects.filter(location='pune')
     context={'pune_data':pune_data}
     return render(request,'pune_data.html',context)
    else:
     cname=request.POST.get('cname')
     chennai_data=EmployeeData.objects.filter(Q(location='chennai') & Q(company=cname))
     context={'chennai_data':chennai_data}
     return render(request,'chennai_data.html',context)
