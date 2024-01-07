from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
from django.http import HttpResponse
def create_topic(request):
    
    if request.method=="POST":
        tnm=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tnm)[0]
        TO.save()
        return HttpResponse('data is inserted')
    return render(request,'htmlform.html')
def create_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d={'QLWO':QLWO}
        return render(request,'display_webpage.html',d)
    return render(request,'webpage.html',d)
def create_access(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']
        WO=Webpage.objects.get(pk=na)
        AO=AccessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d={'QLAO':QLAO}
        return render(request,'display_access.html',d)
    return render(request,'insert_access.html',d)
def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in tn:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        di={'QLWO':QLWO}
        return render(request,'display_webpage.html',di)
    return render( request,'select_multiple_webpage.html',d)
#def select_multiple_access(request):
def select_multiple_access(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST.getlist('na')
        QLAO=AccessRecord.objects.none()
        for i in na:
            QLAO=QLAO|AccessRecord.objects.filter(pk=i)
        di={'QLAO':QLAO}
        '''dt=request.POST['dt']
        au=request.POST['au']
        AO=AccessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        di={'QLAO':QLAO}'''
        
        return render(request,'display_access.html',di)
    
    return render(request,'select_multiple_access.html',d)
def check_box(request):
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        
        return render(request,'check_box.html',d)
def check_box_access(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST.getlist('na')
        QLAO=AccessRecord.objects.none()
        for i in na:
            QLAO=QLAO|AccessRecord.objects.filter(pk=i)
        di={'QLAO':QLAO}
        return render(request,'display_access.html',di)
    return render(request,'check_box_access.html',d)
    
        
    
    

        

