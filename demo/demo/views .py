from django.http import HttpResponse
from django.shortcuts import render

def demo2(req):
    return HttpResponse('welcome to demo 2')
def demo4(req):
    return render(req,'example.html')