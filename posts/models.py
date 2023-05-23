from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    condition_choices = [
        ('or','Never Worn, with Original Tags'),('ne','Never Worn'),
        ('vg','Very Good Condition'),('gd','Good Condition'),('fr','Fair Condition'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name', default='General')
    color = models.CharField(max_length=255, default='undefined')
    dimensions = models.CharField(max_length=255, default='undefined')
    cost = models.CharField(max_length=255, default='undefined')
    address = models.CharField(max_length=510, default='undefined')
    condition = models.CharField(
        max_length=32, choices=condition_choices, default='normal'
    )
    image = models.ImageField(
        upload_to='images/', default='../default_post_m09zvf', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'