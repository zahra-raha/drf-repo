from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_lf3xxw'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}'s profile"


def create_profile(sender, instance, created, **kwangs):
    if created:
        Profile.objects.create(owner=instance)


models.signals.post_save.connect(create_profile, sender=User)

# Create your models here.
