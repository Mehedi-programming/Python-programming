from django.http import HttpResponse

from django.shortcuts import render,redirect
from . models import *
def home(req):
    about_data=ABOUT.objects.get(id=7)
    education_data=EDUCATION.objects.all()
    experience_data=EXPERIENCE.objects.all()#
    resarch_data=RESARCH.objects.all()#
    funfact_data=FUNFACT.objects.get(id=4)
    skill_data=SKILL.objects.get(id=2)
    testimonial_data=TESTIMONIAL.objects.get(id=1)
    service_data=SERVICE.objects.get(id=3)
    contact_data=CONTACT.objects.get(id=1)
    homepage_data=HOMEPAGE.objects.get(id=2)
    data = {'ab_data':about_data,'edu_data':education_data,'exp_data':experience_data,'res_data':resarch_data,'fun_data':funfact_data,'sk_data':skill_data,'test_data':testimonial_data,'ser_data':service_data,'cont_data':contact_data,'home_data':homepage_data}
    return render(req,'index.html',data)

def about(req):
    all_data=ABOUT.objects.all()
    data={'about_d':all_data}
    return render(req,'about.html',data)

def education(req):
    all_data=EDUCATION.objects.all()
    data={'education_d':all_data}
    return render(req,'education.html',data)

def experience(req):
    all_data=EXPERIENCE.objects.all()
    data={'experience_d':all_data}
    return render(req,'experience.html',data)

def resarch(req):
    all_data=RESARCH.objects.all()
    data={'resarch_d':all_data}
    return render(req,'resarch.html',data)

def funfact(req):
    all_data=FUNFACT.objects.all()
    data={'funfact_d':all_data}
    return render(req,'funfact.html',data)

def skill(req):
    all_data=SKILL.objects.all()
    data={'skill_d':all_data}
    return render(req,'skill.html',data)

def testimonial(req):
    all_data=TESTIMONIAL.objects.all()
    data={'testimonial_d':all_data}
    return render(req,'testimonial.html',data)


def service(req):
    all_data=SERVICE.objects.all()
    data={'service_d':all_data}
    return render(req,'service.html',data)


def contact(req):
    all_data=CONTACT.objects.all()
    data={'contact_d':all_data}
    return render(req,'contact.html',data)


def homepage(req):
    all_data=HOMEPAGE.objects.all()
    data={'homepage_d':all_data}
    return render(req,'homepage.html',data)


def aboutInsert(req):
    tittle= req.POST.get('tittle')
    description= req.POST.get('description')
    name = req.POST.get('name')
    age = req.POST.get('age')
    occupation = req.POST.get('occupation')
    phone = req.POST.get('phone')
    email = req.POST.get('email') 
    nationality = req.POST.get('nationality')
    my_image = req.FILES.get('img')

    about_obj = ABOUT()
    about_obj.Tittle=tittle
    about_obj.Description=description
    about_obj.Name=name
    about_obj.Age=age
    about_obj.Occupation=occupation
    about_obj.Phone=phone
    about_obj.Email=email
    about_obj.Nationality=nationality
    about_obj.S_image=my_image

    about_obj.save()
    return redirect('about_home')

def educationInsert(req):
    degree_department= req.POST.get('degree_department')
    institute= req.POST.get('institute')
    session= req.POST.get('session')
    description= req.POST.get('description')

    education_obj = EDUCATION()
    education_obj.Degree_department=degree_department
    education_obj.Institute=institute
    education_obj.Session=session
    education_obj.Description=description

    education_obj.save()
    return redirect('education_home')

def experienceInsert(req):
    position = req.POST.get('position')
    company_name = req.POST.get('company_name')
    time = req.POST.get('time')
    representation = req.POST.get('representation')

    experience_obj = EXPERIENCE()
    experience_obj.Position=position
    experience_obj.Company_name=company_name
    experience_obj.Time=time
    experience_obj.Representation=representation

    experience_obj.save()
    return redirect('experience_home')

def resarchInsert(req):
    resarch_name = req.POST.get('resarch_name')
    description = req.POST.get('description')
    time = req.POST.get('time')

    resarch_obj = RESARCH()
    resarch_obj.Resarch_name=resarch_name
    resarch_obj.Description=description
    resarch_obj.Time=time

    resarch_obj.save()
    return redirect('resarch_home')

def funfactInsert(req):
    tittle = req.POST.get('tittle')
    description = req.POST.get('description')
    experience_year = req.POST.get('experience_year')
    client_count = req.POST.get('client_count')
    project_count= req.POST.get('project_count')
    digital_products = req.POST.get('digital_products')

    funfact_obj = FUNFACT()
    funfact_obj.Tittle=tittle
    funfact_obj.Description=description
    funfact_obj.Experience_year=experience_year
    funfact_obj.Client_count=client_count
    funfact_obj.Project_count=project_count
    funfact_obj.Digital_products=digital_products

    funfact_obj.save()
    return redirect('funfact_home')

def skillInsert(req):
    tittle = req.POST.get('tittle')
    description = req.POST.get('description')
    html_percantage = req.POST.get('html_percantage')
    css_percantage = req.POST.get('css_percantage')
    python_percantage = req.POST.get('python_percantage')
    javaScript_percantage = req.POST.get('javaScript_percantage')
    research=req.POST.get('research')

    skill_obj = SKILL()
    skill_obj.Tittle=tittle
    skill_obj.Description=description
    skill_obj.HTML_percantage=html_percantage
    skill_obj.CSS_percantage=css_percantage
    skill_obj.Python_percantage=python_percantage
    skill_obj.JavaScript_percantage=javaScript_percantage
    skill_obj.Research=research

    skill_obj.save()
    return redirect('skill_home')

def testimonialInsert(req):
    tittle = req.POST.get('tittle')
    description = req.POST.get('description')
    client_name = req.POST.get('client_name')
    company_name = req.POST.get('company_name')
    articles = req.POST.get('articles')

    testimonial_obj = TESTIMONIAL()
    testimonial_obj.Tittle=tittle
    testimonial_obj.Description=description
    testimonial_obj.Client_name=client_name
    testimonial_obj.Company_name=company_name
    testimonial_obj.Articles=articles 

    testimonial_obj.save()
    return redirect('testimonial_home')

def serviceInsert(req):
    tittle1web = req.POST.get('tittle1web')
    tittle2security = req.POST.get('tittle2security')

    service_obj = SERVICE()
    service_obj.Tittle_1_web=tittle1web
    service_obj.Tittle2_security=tittle2security

    service_obj.save()
    return redirect('service_home')

def contactInsert(req):
    tittle = req.POST.get('tittle')
    location = req.POST.get('location')
    phone = req.POST.get('phone')
    email = req.POST.get('email')

    contact_obj = CONTACT()
    contact_obj.Tittle=tittle
    contact_obj.Location=location
    contact_obj.Phone=phone
    contact_obj.Email=email

    contact_obj.save()
    return redirect('contact_home')

def hompageInsert(req):
    name = req.POST.get('name')
    article = req.POST.get('article')

    homepage_obj = HOMEPAGE()
    homepage_obj.Name=name
    homepage_obj.Article=article

    homepage_obj.save()
    return redirect('homepage_home')