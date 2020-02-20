from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import(
    AuthenticationForm
)
from .models import Plan

class LoginForm(AuthenticationForm):
    #ログオンフォームの定義
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['class'] = 'form-control'
            fields.widget.attrs['placeholder']= fields.label

class MenuForm(forms.Form):
    name = forms.CharField(
        label='メニュー', max_length=50,
        required=False
    )
    isRepeat = forms.BooleanField(
        label='毎週'
    )
  
    def save(self):
        name = self.cleaned_data.get('name')
        print(name ,"ee")
        p = Plan(year=2020,month=2, day=1, menu=name, isRow=True)
        p.save()

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'This does not match with the above.')

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        new_user = User.objects.create_user(username = username)
        new_user.set_password(password)
        new_user.save()