from django.http import HttpResponse

from django.shortcuts import render,redirect
from . models import ABOUT
from . models import Education

def home(req):
    single_data=ABOUT.objects.get(id=31)
    service_data=Education.objects.get(id=2)
    data = {'d':single_data,'s_data':service_data}
    return render(req,'index.html',data)

def about(req):
    all_data=ABOUT.objects.all()
    data={'about_d':all_data}
    return render(req,'about.html',data)

def aboutEdit(req,uid):
    single_data=ABOUT.objects.get(id=uid)
    data={'d':single_data}
    return render(req,'edit.html',data)
    
    #all_data=ABOUT.objects.all()
    #data={'about_d':all_data}
   #return render(req,'about.html',data)

def aboutDel(req,uid):
    single_data=ABOUT.objects.get(id=uid)
    single_data.delete()
    return redirect('about_home')

def aboutInsert(req):
    name = req.POST.get('name')#this 'name'  will come from form
    age = req.POST.get('age')
    occupation = req.POST.get('occupation')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    nationality = req.POST.get('nationality')

    about_obj = ABOUT()
    about_obj.Name=name
    about_obj.Age=age 
    about_obj.Occupation=occupation
    about_obj.Phone=phone
    about_obj.Email=email
    about_obj.Nationality=nationality

    about_obj.save()
    return redirect('about_home')#action url/reverse url for showing in same page


def aboutUpdate(req):
    id=req.POST.get('uid')
    name = req.POST.get('name')
    age = req.POST.get('age')
    occupation = req.POST.get('occupation')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    nationality = req.POST.get('nationality')

    about_obj = ABOUT.objects.get(id=id)
    about_obj.Name=name
    about_obj.Age=age
    about_obj.Occupation=occupation
    about_obj.Phone=phone
    about_obj.Email=email
    about_obj.Nationality=nationality

    about_obj.save()
    return redirect('about_home')

def home(req):
    single_data=Education.objects.get(id=2)
    data = {'d':single_data}
    return render(req,'index.html',data)

def education(req):
    all_data=Education.objects.all()
    data={'education_d':all_data}
    return render(req,'edu.html',data)

def educationEdit(req,id):
    single_data=Education.objects.get(id=id)
    data={'d':single_data}
    return redirect('eduEdit.html',data)
    
    #all_data=ABOUT.objects.all()
    #data={'about_d':all_data}
   #return render(req,'about.html',data)

def educationDel(req,id):
    single_data=Education.objects.get(id=id)
    single_data.delete()
    return redirect('education_home')

def educationInsert(req):
    degree = req.POST.get('degree')
    institute = req.POST.get('institute')
    session = req.POST.get('session')
    description = req.POST.get('description')
    result = req.POST.get('result')

    education_obj = Education()
    education_obj.Degree=degree
    education_obj.Institute=institute
    education_obj.Session=session
    education_obj.Description=description
    education_obj.Result=result

    education_obj.save()
    return redirect('education_home')



def educationUpdate(req):
    id=req.POST.get('id')
    degree = req.POST.get('degree')
    institute = req.POST.get('institute')
    session = req.POST.get('session')
    description = req.POST.get('description')
    result = req.POST.get('result')
    

    education_obj = Education.objects.get(id=id)
    education_obj.Degree=degree
    education_obj.Institute=institute
    education_obj.Session=session
    education_obj.Description=description
    education_obj.Result=result


    education_obj.save()

    return redirect('education_home')




    #return  HttpResponse(name)

    #return render(req,'about.html')