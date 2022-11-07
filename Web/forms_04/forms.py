from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=30,
                           label="Your Name",
                           help_text="Enter your name",
                           widget=forms.TextInput(
                                # this correspodnds to HTML Attributes
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

    OCCUPANCIES = (
        (1, 'Child'),
        (2, "High School Student"),
        (3, "Student"),
    )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select,
    )

    occupancy_2 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect(),
    )
