from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Newuserform(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(Newuserform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
