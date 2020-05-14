"""Hospital_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from  app.views import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='main'),
    path('aboutus/',aboutus,name='aboutus'),
    path('contactus/',contactus,name='contactus'),
    path('admin_login/',admin_login,name='admin_login'),
    path('admin_home/',admin_home,name='admin_home'),
    path('admin_logout/',admin_logout,name='admin_logout'),
    path('add_doctor/',add_doctor,name='add_doctor'),
    path('view_doctor/',view_doctor,name='view_doctor'),
    path('delete_doctor/',delete_doctor,name='delete_doctor'),
    path('add_patient/',add_patient,name='add_patient'),
    path('view_patient/',view_patient,name='view_patient'),
    path('delete_patient/',delete_patient,name='delete_patient'),
    path('add_appointment/',add_appointment,name='add_appointment'),
    path('view_appointment/',view_appointment,name='view_appointment'),
    path('delete_appointment/',delete_appointment,name='delete_appointment')

]