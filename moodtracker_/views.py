from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Moodtracker
from django.views.generic import TemplateView
from moodtracker_.forms import MoodtrackerForm


class MoodtrackerView(TemplateView):
    template_name = 'moodtrackerHome.html'

    def get(self, request):
        form = MoodtrackerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MoodtrackerForm(request.POST)
        if form.is_valid():
            form.save()
#            text = form.cleaned_data['date', 'mood', 'activities']
            form = MoodtrackerForm()
            return redirect('history/')
        args = {'form': form, 'text': text,}
        return render(request, self.template_name, args)


# Create your views here.
def index(request):
    all_moodtrackers = Moodtracker.objects.all()
    return render(request, 'moodtracker/index.html', {'all_moodtrackers': all_moodtrackers})


def detail(request, moodtracker_id):
    try:
        moodtracker = Moodtracker.objects.get()
    except Moodtracker.DoesNotExist:
        raise Http404("Moodtracker Entry does not exist")
    return render(request, 'moodtracker/details.html', {'moodtracker': moodtracker})

# Create your views here.
'''
<!DOCTYPE html>
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
  </form>
{% endblock %}
'''