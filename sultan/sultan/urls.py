"""
URL configuration for sultan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('mehedi/',views.home),
    path('about/',views.about,name='about_home'),
    path('education/',views.education,name='education_home'),
    path('experience/',views.experience,name='experience_home'),
    path('resarch/',views.resarch,name='resarch_home'),
    path('funfact/',views.funfact,name='funfact_home'),
    path('skill/',views.skill,name='skill_home'),
    path('testimonial/',views.testimonial,name='testimonial_home'),
    path('service/',views.service,name='service_home'),
    path('contact/',views.contact,name='contact_home'),
    path('homepage/',views.homepage,name='homepage_home'),
    path('about/insert',views.aboutInsert,name='about_insert'),
    path('education/insert',views.educationInsert,name='education_insert'),
    path('experience/insert',views.experienceInsert,name='experience_insert'),
    path('resarch/insert',views.resarchInsert,name='resarch_insert'),
    path('funfact/insert',views.funfactInsert,name='funfact_insert'),
    path('skill/insert',views.skillInsert,name='skill_insert'),
    path('testimonial/insert',views.testimonialInsert,name='testimonial_insert'),
    path('service/insert',views.serviceInsert,name='service_insert'),
    path('contact/insert',views.contactInsert,name='contact_insert'),
    path('homepage/insert',views.hompageInsert,name='homepage_insert'),
   #path('about/edit',views.aboutUpdate,name='about_update'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
