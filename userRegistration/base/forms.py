from django import forms
from .models import user

class signupform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class loginForm(forms.ModelForm):
    
    class Meta:
        model = user
        fields = '__all__'

