from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter username'})
    )

    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={'class':'input','placeholder':'Enter password'})
    )

class SignUpForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter firstname'})
    )

    last_name = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter lastname'})
    )

    username = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'})
    )

    password = forms.CharField(
        required=True,
        min_length=4,
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'})
    )