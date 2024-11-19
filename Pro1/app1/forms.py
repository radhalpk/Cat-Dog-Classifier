from django import forms
from app1 import models

class UserForm(forms.ModelForm):
    
    class Meta:
        model = models.UserModel
        fields = '__all__'