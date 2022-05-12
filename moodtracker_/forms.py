from django import forms
from moodtracker_.models import Moodtracker

class MoodtrackerForm(forms.ModelForm):
    class Meta:
        model = Moodtracker
        fields = ('date', 'mood', 'activities')