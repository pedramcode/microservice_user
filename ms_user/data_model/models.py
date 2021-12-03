from django.db import models
from django.contrib.auth.models import User


class DataModel(models.Model):
    is_deleted = models.BooleanField(default=False, verbose_name="Is deleted")
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        abstract = True


class UserDataModel(DataModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    class Meta:
        abstract = True
