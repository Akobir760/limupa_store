from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)

    def clean(self):
        username_or_email = self.cleaned_data['username_or_email']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(
                Q(email=username_or_email) | Q(username=username_or_email)
            )
        except User.DoesNotExist:
            raise forms.ValidationError("Username or password is invalid")

        credentials = {"username": user.username, "password": password}
        authenticated_user = authenticate(**credentials)
        if authenticated_user is not None:
            self.cleaned_data["user"] = authenticated_user
        else:
            raise forms.ValidationError("Username or password is invalid")

        return self.cleaned_data