from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username=username_to_toggle)
        user = request_user
        # todo по сути связей как таковых нет, просто добавление и удалений из масссива?
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True # todo почему из фоловин меняется и в модели и в вьюхе, в чем логика?

        return profile_, is_following


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)


post_save.connect(post_save_user_receiver, sender=User)
