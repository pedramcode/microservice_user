from django.db import models
from data_model.models import UserDataModel


class Profile(UserDataModel):
    mobile = models.CharField(max_length=50, verbose_name="Mobile number", blank=True, null=True)
    bio = models.TextField(max_length=255, verbose_name="Bio", blank=True, null=True)

    def __str__(self):
        return self.user.username
