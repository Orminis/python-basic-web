from django.urls import path

from apps.forms_04.views import index_forms, index_model_forms, related_models_demo

urlpatterns = (
    path('', index_forms, name='index forms'),
    path('modelforms/', index_model_forms, name='model forms'),
    path('demo_relations/', related_models_demo, name='demo relations')
)
