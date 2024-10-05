from django.http import HttpResponse

from django.shortcuts import render
from . models import About
def demo2(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def aboutInsert(req):
    contuct=req.POST.get('contuct')
    desc=req.POST.get('desc')
    email=req.POST.get('email')
    fb=name=req.POST.get('fb')
    phone=name=req.POST.get('phone')
    git=req.POST.get('git')
    return HttpResponse(name)
    #return render(req,'about.html')
    about_obj=About()
    about_obj.contuct=contuct
    about_obj.description=desc
    about_obj.email=email
    about_obj.fb=fb
    about_obj.phone=phone
    about_obj.git=git
