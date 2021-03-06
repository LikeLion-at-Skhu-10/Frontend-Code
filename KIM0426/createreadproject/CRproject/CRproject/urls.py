"""CRproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
import CRapp.views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CRapp.views.home,name = 'home'),
    path('new/',CRapp.views.new,name = 'new'),
    path('create/',CRapp.views.create,name = 'create'),
    path('formC/',CRapp.views.formC,name = 'formC'),
    path('modelformC/',CRapp.views.modelformC,name = 'modelformC'),
    path('detail/<int:blog_id>',CRapp.views.detail,name = 'detail'),
    path('register/',CRapp.views.register,name = 'register'),
    path('register_study/',CRapp.views.register_study,name = "register_study"),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
