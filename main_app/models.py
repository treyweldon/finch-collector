from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
   ('M', 'Morning'),
   ('E', 'Evening')
)

# Create your models here.
class Accessory(models.Model):
  name = models.CharField(max_length=50)
  material = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('acc_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    accessory = models.ManyToManyField(Accessory)

    def __str__(self):
        return f'{self.name}({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  # Create a cat_id FK
  finch = models.ForeignKey(
    Finch,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
