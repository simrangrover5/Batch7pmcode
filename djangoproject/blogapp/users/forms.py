from django import forms

class Login(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput)


class Signup(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    pic = forms.ImageField()