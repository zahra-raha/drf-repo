from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} follows {self.followed}'
# Create your models here.
