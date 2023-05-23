from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class UserType(models.Model):
    userType = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.userType


class User(AbstractUser):
    """
    Default custom user model for qna.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    name = models.CharField(_("닉네임"), null=True, max_length=255)
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(null=True, max_length=255)
    email = models.CharField(null=True, max_length=255)
    

    # first_name = None  # type: ignore
    # last_name = None  # type: ignore
       

    def __str__(self):
        return "%s"%self.name
    # First and last name do not cover name patterns around the globe


    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
