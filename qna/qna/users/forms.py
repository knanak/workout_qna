from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms as dj_forms
from . import models

User = get_user_model()

class UsertypeForm(dj_forms.ModelForm):
    class Meta:
        model=models.UserType
        fields='__all__'

class RegistrationForm(dj_forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'user_type', 'name', 'email', 'password']
        widgets= {'password': dj_forms.PasswordInput(),}
        labels={'user_type':'사용자 유형', 'name':'닉네임'}

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit :
            user.save()
            return user

class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
