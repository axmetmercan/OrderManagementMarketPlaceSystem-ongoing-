from tkinter.tix import Form
from django import forms


class Registration(forms.Form):
    user_name = forms.CharField(max_length= 50, label='User Name')
    password = forms.CharField(max_length= 20, label='Password', widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label='Repassword', widget= forms.PasswordInput)
    


    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')


        if password and confirm and password != confirm:
            raise forms.ValidationError('Missmatch Passwords')
        

        values = {
            'user_name' : user_name,
            'password' : password,
        }
        return values

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=20, label='Şifre', widget=forms.PasswordInput)