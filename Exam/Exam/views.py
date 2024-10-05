from django.http import HttpResponse

from django.shortcuts import render,redirect
from . models import About 
def home(req):
    single_data=About.objects.get(id=1)
    data={'d':single_data}

    return render(req,'index.html',data)
def about(req):
    all_data=About.objects.all()#queryset
    data={'about_d':all_data}
    return render(req,'index2.html',data)

   
   #single_data=About.objects.get(id=1)
    #data={'d':single_data}
def aboutEdit(req,uid):
    single_data=About.objects.get(id=uid)
    data={'d':single_data}
    return render(req,'edit.html',data)

def aboutInsert(req):
    name = req.POST.get('name')
    desc = req.POST.get('desc')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    fb = req.POST.get('fb')
    github = req.POST.get('github')
    gmail = req.POST.get('gmail')

    about_obj=About()

    about_obj.name=name
    about_obj.description=desc
    about_obj.phone=phone
    about_obj.email=email
    about_obj.fb=fb
    about_obj.github=github
    about_obj.gmail=gmail

    about_obj.save()

def aboutUpdate(req):
    name = req.POST.get('name')
    desc = req.POST.get('desc')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    fb = req.POST.get('fb')
    github = req.POST.get('github')
    gmail = req.POST.get('gmail')

    about_obj=Aboutobjects.get(id=id)

    about_obj.name=name
    about_obj.description=desc
    about_obj.phone=phone
    about_obj.email=email
    about_obj.fb=fb
    about_obj.github=github
    about_obj.gmail=gmail

    about_obj.save()
    

    return redirect('about_home')



    #return render(req,'index2.html')