"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # first lecture introduction
    # SITE_URL/tasks/ (localhost:8000/tasks/)
    path("introduction/", include('Web.django_introduction_01.urls')),

    # urls from second lecture
    path('departments/', include('Web.departments_02.urls')),

    # urls from third lecture
    path('models/', include('Web.models_03.urls')),

    # urls from forth lecture
    path('forms/', include('Web.forms_04.urls')),
]
