from django.urls import path

from Web.forms_04.views import index_forms

urlpatterns = (
    path('', index_forms, name='index forms'),

)
