from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.db.models import fields

from users.models import AccountType, User, Profile


class AccountTypeForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=AccountType.objects.all())

    class Meta:
        fields = ['name']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name :", widget=forms.TextInput(
        attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(label="Last Name:", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(label="Email :", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    username = forms.CharField(label="Username :", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label="Password : ", required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label="Password Confirmation: ", required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Your Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    accountType = forms.ModelChoiceField(label="Account Type: ",
                                         queryset=AccountType.objects.all())

    class Meta:
        model = Profile
        fields = ['image', 'occupation', 'age', 'accountType', ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
