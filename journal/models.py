from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    date = models.CharField(max_length=100)
    entry = models.CharField(max_length=2500)

    def get_absolute_url(self):
       return reverse('journal:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.date + ' - ' + self.entry
