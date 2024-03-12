from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}({self.id})'