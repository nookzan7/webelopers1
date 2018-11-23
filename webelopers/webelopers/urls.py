"""webelopers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from Main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signUp/',views.sign_up),
    path('createUser/',views.create_user,name='createUser'),
    path('login/',views.login_),
    path('logout/',views.logout_),
    path('contactUs/',views.contact_us),
    path('contactSaved/',views.contact_saved,name="contactSaved")
    #re_path(r'.*',views.home), todo:make exceptions for urls which are already here

]
