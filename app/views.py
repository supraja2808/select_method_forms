from django.shortcuts import render

# Create your views here.
from app.models import *



def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=="POST":
        topic_name=request.POST['topic_name']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topic_name)
        QSWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        QSWO.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1) 
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    
    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['date']
        author=request.POST['author']
        email=request.POST['email']
        WO=Webpage.objects.get(pk=name)
        QSAO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author,email=email)[0]
        QSAO.save()
        QSAO=AccessRecord.objects.all()
        d1={'QSAO':QSAO}
        return render(request,'display_accessrecord.html',d1) 

    return render(request,'insert_accessrecord.html',d)


def select_and_display(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        print(tnlist)

        QSWO=Webpage.objects.none()

        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=tn)

        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)   


    return render(request,'select_and_display.html',d)