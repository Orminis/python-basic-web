from django.urls import path

from apps.django_introduction_01.views import does_it_works, get_all_tasks, index

urlpatterns = (
    # localhost:8000/tasks/
    path("", index),
    # localhost:8000/tasks/is-it/
    path("is-it", does_it_works),
    # localhost:8000/tasks/create
    path("all/", get_all_tasks),
)
