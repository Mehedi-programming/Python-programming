#from django.http import HttpResponse
from django.shortcuts import render

def demo1(req):
    return render(req,'example.html')
def demo2(req):
    return HttpResponse('welcome to my website no 2')
def demo3(req): 
    a=40
    b=12
    product_price=[1,2,3,4,5,5]
    sum=a+b
    sub=a-b
    data={'d':sum,'c':sub,'prod':product_price}
    return render(req,'example2.html',data)
   