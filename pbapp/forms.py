from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    motivational_text = forms.CharField(widget=forms.Textarea, label='Motivational Text')
    age = forms.IntegerField(label='Age')
    location = forms.CharField(max_length=100, label='Location')
    hobbies = forms.CharField(max_length=100, label='Hobbies')
    shirt_size = forms.CharField(max_length=10, label='Shirt Size')
    pants = forms.CharField(max_length=10, label='Pants Size')
    gender = forms.CharField(max_length=10, label='Gender')
    occupation = forms.CharField(max_length=100, label='Occupation')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'motivational_text', 'age', 'location', 'hobbies', 'shirt_size', 'pants', 'gender', 'occupation']
