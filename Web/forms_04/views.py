from django import forms
from django.shortcuts import render

# Create your views here.
from Web.forms_04.forms import PersonForm, PersonCreateForm
from Web.forms_04.models import Person, Pet


def index_forms(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    # we receive the form and data from the http request
    else:
        # request.method == 'post':
        form = PersonForm(request.POST)

        # `is_valid()`: validates the form, returns True or false
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


def index_model_forms(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }

    return render(request, 'forms/model_forms.html', context)


def related_models_demo(request):
    pet = Pet.objects.get(pk=1)
    person = Person.objects.get(pk=1)
    # person.pets  # Person has `pets` field
    # pet.person_set  # Pet has no `person` field
    # print(list(pet.person_set.all()))
    print(list(pet.persons.all()))
    print(list(person.pets.all()))
