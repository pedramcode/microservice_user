from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile


def save_profile(sender, instance, **kwargs):
    if Profile.objects.filter(user=instance).count() == 0:
        Profile.objects.create(user=instance)


post_save.connect(save_profile, sender=User)
