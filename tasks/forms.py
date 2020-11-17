from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'title': forms.Textarea(attrs={'cols': 50, 'rows': 1}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 6})
        }

class TaskDoneForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'complete'}

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }