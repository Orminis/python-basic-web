from django.urls import path

from Web.models_03.views import info, show_department, delete_employee

urlpatterns = (
    path("", info, name='info'),
    path("departments/<int:pk>", show_department, name="details department"),
    path("delete/<int:pk>/<slug:slug>/", delete_employee, name="delete employee"),
)
