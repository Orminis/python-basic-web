from django.urls import path

from Web.departments_02.views import show_departments, show_department_id, redirect_to_first_department, \
    show_not_found

urlpatterns = (
    # /departments/
    path("", show_departments, name="show departments"),

    # redirect
    # /departments/redirect/
    path("redirect/", redirect_to_first_department, name="redirect demo"),

    # /departments/{department_ID}
    path("<department_id>/", show_department_id, name="show department details with string"),

    # /departments/int/{department_ID}
    path("int/<int:department_id>/", show_department_id, name="show department details"),

    # erro message
    path("not-found", show_not_found),
)
