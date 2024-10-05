from django.http import HttpResponse

def demo1(req):
    return render(req,'index.html')
def demo2(req):
    return HttpResponse('welcome to my website no 2')