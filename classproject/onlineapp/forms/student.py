from django import forms

from onlineapp.models import College,Student,MockTest1

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude= ['id','college']
        #name,email,db_folder,dropped_out
        widgets = {
            'name': forms.TextInput(attrs = {'class':'input','placeholder':'Enter Name'}),
            'email': forms.EmailInput(attrs = {'class':'input','placeholder':'Enter email address'}),
            'db_folder': forms.TextInput(attrs= {'class':'input', 'placeholder':'Enter DB Folder name'}),
            'dropped_out': forms.CheckboxInput(),
            'dob' : forms.DateInput(attrs={'type':'date'})
        }

class MockTestForm(forms.ModelForm):
    class Meta:
        model = MockTest1

        exclude = ['total','student','id']

        widgets = {
            'problem1':forms.NumberInput(attrs = {'class': 'input', 'placeholder': 'Problem 1'}),
            'problem2': forms.NumberInput(attrs= {'class': 'input', 'placeholder': 'Problem 2'}),
            'problem3': forms.NumberInput(attrs= {'class': 'input', 'placeholder': 'Problem 3'}),
            'problem4': forms.NumberInput(attrs= {'class': 'input', 'placeholder': 'Problem 4'})
        }

