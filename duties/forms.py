from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'login'})
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )
