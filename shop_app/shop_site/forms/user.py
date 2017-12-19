
# Login form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from shop_app.models import User

input_class = 'form-control placeholder-no-fix'

class LoginForm(forms.Form):
    email = forms.CharField(widget= forms.EmailInput(attrs= {'placeholder': 'email@domain.com', 'class':input_class}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':input_class}))

class RegisterForm(UserCreationForm):
     name = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Name','class':input_class}))

     last_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': input_class}))

     address = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'placeholder':'Address', 'class': input_class}))

     email = forms.EmailField(required=True,
                              widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': input_class}))

     password1 = forms.CharField(required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': input_class}))

     password2 = forms.CharField(required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': input_class}))

     class Meta:
         model = User
         fields = ('last_name', 'first_name', 'email', 'password1', 'password2')

     def save(self, commit=True):
         user = super(UserCreationForm, self).save(commit=False)
         user.set_password(self.cleaned_data["password1"])

         if commit:
             user.save()

         return user
