from django.shortcuts import render
from django.db.models import Q
from .models import Delboys,Area,DrsData,Dummydrs
from recdata.models import Recievedata
from django.contrib import messages
# Create your views here.
def drs_index(request):
    return render(request,'drs_index.html')
def generate_drs(request):
    global c
    boys = Delboys.objects.all()
    area = Area.objects.all()
    condata = Recievedata.objects.all()
    drsdata = DrsData()
    boylast = Delboys.objects.last()
    #arealast = Area.objects.last()
    drsdb = DrsData.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        drsno = request.POST.get('drsno')
        boy = request.POST.get('delboyselect')
        area = request.POST.get('areaname')
        conno = request.POST.get('conno')
        #dudrs.save()
        for c in condata:
            try:
                if c.conno == conno:
                    drsdata.conno = c.conno
                    drsdata.pcs = c.pcs
                    drsdata.wth = c.wt
                    drsdata.date = date
                    drsdata.drsno = drsno
                    drsdata.boy = boy
                    drsdata.area = area
                    drsdata.save()
                    #dudrs.dummydrs = drsno
                    #dudrs.save()
                    messages.info(request,'added')
                    return render(request,'drs_generate.html',{'boys':boys,'areas':area,'boylast':boylast,'drsdb':drsdb,'con':request.POST.get('drsno')})
                else:
                    c=0                  
                    c+=1    
            except Exception as e:
                messages.info(request,'Not found')
                return render(request,'drs_generate.html',{'boys':boys,'areas':area,'boylast':boylast,'drsdb':drsdb,'con':request.POST.get('drsno')})
        if c>0 :
                messages.info(request,'Not Found')
        
    return render(request,'drs_generate.html',{'boys':boys,'areas':area,'boylast':boylast,'drsdb':drsdb,'con':request.POST.get('drsno')})


def display_drs(request):
    drsnosearch = request.POST.get('drsnosearch')
    drsdata_search = DrsData.objects.all()
    if request.method == 'POST':
        drsnosearch = request.POST.get('drsnosearch')
        drsdata_search = DrsData.objects.all()
        return render(request,'display_drs.html',{'drs':drsdata_search,'drsnosearch':drsnosearch})
    return render(request,'display_drs.html',{'drs':drsdata_search,'drsnosearch':drsnosearch})