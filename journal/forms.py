from django import forms
from journal.models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        entry = forms.CharField(widget=forms.Textarea)
        fields = ('date', 'entry',)

'''
journalHome.html
<form action = "" method = "get">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name">
    <input type="submit" value="OK">
</form>
'''
'''
index.html
<form action = "" method = "get">
    <label for="date">Date: </label>
    <input id="date" type="text" name="date">
    <label for="entry">Enter Your Journal Entry: </label>
    <input id="entry" type="text" name="entry">
    <input type="submit" value="OK">
</form>
'''