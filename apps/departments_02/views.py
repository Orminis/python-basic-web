from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
# without render()
# def show_departments(request, *args, **kwargs):
#     print(request.method)
#     print(request.GET)
#     print(request.POST)
#     print(request.get_host())
#     print(request.get_port())
#     print(request.headers)
#     print(request.path)
#     body = f"path: {request.path} args={args}, kwargs={kwargs}"
#
#     return HttpResponse(body)

# with render
from django.shortcuts import render, redirect


def show_departments(request, *args, **kwargs):
    context = {
        "page_title": "Departments",
        "method": request.method,
        "order_by": request.GET.get("order_by", "name")
    }

# render funkciqta idwa ot django shortcuts i renderira w tekst zadadenite method i order_by stoinosti ot context
    # optional argument (empty dict by default)
    return render(request, "departments/all.html", context)


def show_department_id(request, department_id):
    body = f"path: {request.path} id: {department_id}"

    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', "age", "id"]
    order_by = choice(possible_order_by)
    # to = f"/departments/?order_by={order_by}"
    # ^ interpolation string https://docs.djangoproject.com/en/4.1/topics/i18n/translation/

    # може да даде линк към други сайтове
    # to = https://www.google.com

    # search in  google: django redirect with query parameters
    return redirect("show department details", department_id=12)     #named urls gives abstractions


def show_not_found(request):
    # # 1ви начин за връщане на грешки чрез вградени класове в Джанго (това ще работи добре с redirect)
    # return HttpResponseNotFound("Page was not found")

    # 2ри начин за връщане на грешка чрез метода
    # status_code = 400
    # return HttpResponse("Error", status=status_code)

    # 3ти начин чрез вдигане(raise) на Exception (извикваме класа Http404, който приема Exception и му подаваме текста)
    # get_object_or_404(Task)
    raise Http404("Not found")
