from django import forms
from django.contrib.auth.models import User
from .models import Job

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'salary', 'experience', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'salary': forms.NumberInput(attrs={'placeholder': 'e.g. 50000'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'e.g. 2'}),
            'category': forms.Select(),
        }

        