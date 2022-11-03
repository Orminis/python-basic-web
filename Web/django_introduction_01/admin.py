from django.contrib import admin

# Register your models here.
from Web.django_introduction_01.models import Intro


@admin.register(Intro)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "priority", "description")
