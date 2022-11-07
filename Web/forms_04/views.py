from django.shortcuts import render

# Create your views here.
from Web.forms_04.forms import PersonForm
from Web.forms_04.models import Person


def index_forms(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    # we receive the form and data from the http request
    else:
        # request.method == 'post':
        form = PersonForm(request.POST)
        # validates the form, returns True or false
        # fills `cleaned_data`
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            Person.objects.create(name=name, age=age)
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'forms/index.html', context)
