from django.shortcuts import render
from recdata.models import Recievedata
from .models import RecievedDetails
from django.contrib import messages
# Create your views here.
def deldetails_index(request):
    return render(request,'delivereddetails_index.html')
def updatedeldetails(request):  
    searchcoono = request.POST.get('updatecon')
    recdata = RecievedDetails()
    recdetails = Recievedata.objects.all()
    context = {'srch':searchcoono,'recs':recdetails}
    if request.method == 'POST':
        if 'Update' == request.POST.get('update'):
            deldate = request.POST.get('deldate')
            recby = request.POST.get('recby')
            con = request.POST.get('con')
            recdata.consignmentnumber = con
            recdata.delivereddate = deldate
            recdata.recievedby = recby
            recdata.save()
            messages.info(request,"Added")
    return render(request,'updatedeldetails.html',context)
def viewdeldetails(request):
    recdetails = RecievedDetails.objects.all()
    con = request.POST.get('Searchno')
    return render(request,'viewdeldetails.html',{'recdetails':recdetails,'con':con})