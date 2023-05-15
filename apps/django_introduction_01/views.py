from django.shortcuts import render
from django import http

# Create your views here.

from apps.django_introduction_01.models import Intro


def does_it_works(request):
    return http.HttpResponse("Does not works")


def get_all_tasks(request):
    all_tasks = Intro.objects.order_by('id').all()
    result = ', '.join(f"{t.name}({t.id})" for t in all_tasks)
    # [name(id), name(id)]
    return http.HttpResponse(result)


def index(request):
    all_tasks = Intro.objects.order_by('id').all()

    # може да му подаваме обекти които искаме да се визуализират
    context = {
        "title": "The Tasks App!",
        "tasks": all_tasks,
    }
    return render(request, 'django_introduction/index.html', context)
