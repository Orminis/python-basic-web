from django import forms

from apps.forms_04.models import Person


class PersonForm(forms.Form):

    OCCUPANCIES = (
        (1, 'Child'),
        (2, "High School Student"),
        (3, "Student"),
    )

    name = forms.CharField(max_length=30,
                           label="Your Name",
                           help_text="Enter your name",
                           widget=forms.TextInput(
                                # this corresponds to HTML Attributes
                                attrs={
                                    'placeholder': "Enter name",
                                    'class': 'form-control',
                                }
                           )
    )

    age = forms.IntegerField(required=False,
                             label='Your Age',
                             initial=0,
                             widget=forms.NumberInput(),
    )

    story = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
        required=False,
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )


    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select,
    )

    occupancy_2 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect(),
    )

    occupancy3 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.SelectMultiple(),
    )


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name', 'age')
        # exclude = ('pets', )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

        help_texts = {
            'name': 'Your name',
        }

        labels = {
            'age': 'The AGE',
        }
