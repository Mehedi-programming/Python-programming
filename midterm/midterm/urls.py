"""
URL configuration for midterm project.

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

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('mehedi/',views.home),
    #path('about/',views.demo2),
    path('about/',views.about,name='about_home'),#for view
    path('about/insert/',views.aboutInsert, name='about_insert'),#submit
    path('about/edit/<int:uid>',views.aboutEdit, name='about_edit'),
    path('about/edit',views.aboutUpdate, name='about_update'),
    path('about/delete/<int:uid>',views.aboutDel, name='about_delete'),
    path('education/',views.education,name='education_home'),
    path('education/insert/',views.educationInsert, name='education_insert'),
    path('education/edit/<int:uid>',views.educationEdit, name='education_edit'),
    path('education/edit',views.educationUpdate, name='education_update'),
    path('education/delete/<int:uid>',views.educationDel, name='education_delete'),

]
