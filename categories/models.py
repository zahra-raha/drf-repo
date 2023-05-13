from django.db import models

class Category(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=30 , default='fa-regular fa-cubes')

    class Meta:
        ordering = ['-created_at']

    # def name_class(self):
    #     return self.name.split(' ')[0]

    def __str__(self):
        return self.name
