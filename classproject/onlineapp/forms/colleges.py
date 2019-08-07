from django import forms

from onlineapp.models import College

class AddCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude= ['id']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'input','placeholder':'Enter Name'}),
            'location': forms.TextInput(attrs = {'class':'input','placeholder':'Enter location'}),
            'acronym': forms.TextInput(attrs= {'class':'input', 'placeholder':'Enter college acronym'}),
            'contact': forms.EmailInput(attrs = {'class':'input', 'placeholder':'Enter college Contact'})
        }