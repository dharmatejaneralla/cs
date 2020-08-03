from django.shortcuts import render
from django.http import HttpResponse
from .models import Recievedata
from django.contrib import messages
# Create your views here.
def index(request):
    return  render(request,'index.html')
def addco(request):
    if request.method == 'POST':
        try:
            if request.POST.get('msfno') and request.POST.get('date') and request.POST.get('addcon'):
                recdata = Recievedata()
                recdata.mfno = request.POST.get('msfno')
                recdata.date = request.POST.get('date')
                recdata.conno = request.POST.get('addcon')
                recdata.pcs = request.POST.get('pcs')
                recdata.wt = request.POST.get('wt')
                recdata.save()
                messages.success(request,'Added')            
                return render(request,'addco.html',{'obj':obj})
            else:
                messages.info(request,'Enter Details')
                return render(request,'addco.html')
        except Exception as e :
            messages.info(request,'Consignment number already exits')
    return render(request,'addco.html')
def search(request):
    srch = Recievedata.objects.all()
    msfno = request.POST.get('Searchno')
    return  render(request,'search.html',{'srch':srch,'mfno':msfno})
def display(request):
    srch = Recievedata.objects.all()
    mfn = request.POST.get('msfnum')
    return render(request,'display.html',{'dsp':srch,'msfno':mfn})

def docudel(request):
    redata = Recievedata()
    if request.method == 'POST':
        try:
            redata.conno = request.POST.get('addcon')
            redata.mfno = request.POST.get('msfno')
            redata.date = request.POST.get('date')
            redata.pcs = request.POST.get('pcs')
            redata.wt = request.POST.get('wt')
            redata.save()
            messages.info(request,"added")
        except Exception :
            messages.info(request,"Consignment Number Already Exists")
    return render(request,'docudel.html')