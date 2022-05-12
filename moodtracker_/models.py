from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Moodtracker(models.Model):
    date = models.CharField(max_length=100)
    mood_choices = (
        ('Terrible', 'Terrible'),
        ('Bad', 'Bad'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Amazing', 'Amazing'),
    )
#    mood = MultiSelectField(choices=mood_choices)
    mood = models.CharField(max_length=10, choices=mood_choices)
    activities_choices = (
        ('School', 'School'),
        ('Work', 'Work'),
        ('Exercise', 'Exercise'),
        ('Friends/Family', 'Friends/Family'),
        ('Shopping', 'Shopping'),
        ('Reading', 'Reading'),
        ('TV/Movies', 'TV/Movies'),
        ('Relax', 'Relax'),
        ('None', 'None'),
    )
    activities = MultiSelectField(choices=activities_choices)

    def __str__(self):
        return str(self.date)

# Create your models here.
