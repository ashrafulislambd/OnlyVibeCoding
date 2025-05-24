from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .config import university_mappings

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        flag = False
        
        for key in university_mappings:
            domain = university_mappings[key][0]
            if email.endswith(domain):
                flag = True

        if not flag:
            raise forms.ValidationError("The email must be from one of the accepted universities")
            
        return email
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)