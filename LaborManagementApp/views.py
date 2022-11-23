from django.shortcuts import render
from LaborManagementApp.models import Laborer,Supervisor
from django.contrib import messages
from django.http import HttpResponse
from LaborManagementApp.forms import LaborerForms,SupervisorForms

from django.db import connection

def HomePage(request):
    return render(request,'index.html')

def showDetails(request):    
    laborerdata=Laborer.objects.all()
    supervisordata = Supervisor.objects.all()
    detail = {
                'laborerdata': laborerdata,
                'supervisordata' : supervisordata
            }
    return render(request, 'showDetails.html', detail)

def showRunQuery(request):
    return render(request,'showRunQuery.html')

def editLaborer(request,id):
    editLaborerObj=Laborer.objects.get(lab_id=id)
    context={
        "Laborer":editLaborerObj
    }
    return render(request,'editLaborer.html',context)


def updateLaborer(request,id):
    updateLaborer=Laborer.objects.get(lab_id=id)
    form=LaborerForms(request.POST,instance=updateLaborer)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'editLaborer.html',{"Laborer":updateLaborer})


def delLaborer(request,id):
    delLabObj=Laborer.objects.get(lab_id=id)
    context={
        "Laborer":delLabObj
    }
    return render(request,'delLaborer.html',context)


def deletedLaborer(request,id):
    delLabObj=Laborer.objects.get(lab_id=id)
    delLabObj.delete()
    showall=Laborer.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'delLaborer.html',{"Laborer": delLabObj})

def insertLaborer(request):
    if request.method=="POST":
        if request.POST.get('lab_id') and request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('mobile_number') and request.POST.get('email_id') and request.POST.get('password') and request.POST.get('dist_id'):
            saverecord=Laborer()
            saverecord.lab_id=request.POST.get('lab_id')
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.address=request.POST.get('address')
            saverecord.mobile_number=request.POST.get('mobile_number')
            saverecord.email_id=request.POST.get('email_id')
            saverecord.password=request.POST.get('password')
            saverecord.dist_id=request.POST.get('dist_id')

            allval=Laborer.objects.all()
            
            for i in allval:
                if int(i.lab_id)==int(request.POST.get('lab_id')):
                    messages.warning(request,'Laborer already exists....!')
                    return render(request,'insertLaborer.html')

            saverecord.save()
            messages.success(request,'Laborer '+saverecord.name+' is saved succesfully!!')
            return render(request,'insertLaborer.html')
    else:
            return render(request,'insertLaborer.html')


def sortLaborer(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=Laborer.objects.all().order_by(type)
            supervisordata = Supervisor.objects.all()
            context = {
                'laborerdata': sorted,
                'supervisordata' : supervisordata
            }
            return render(request,'showDetails.html',context)
    else:
        return render(request,'showDetails.html')


def RunQuery(request):

    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    colnames = [desc[0] for desc in cursor.description]


    return render(request,'RunQuery.html',{'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

            