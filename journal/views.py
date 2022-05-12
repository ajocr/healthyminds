from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.views import generic
from .models import Journal
from django.views.generic import TemplateView
from journal.forms import JournalForm


# Create your views here.
class JournalView(TemplateView):
    template_name = 'journalHome.html'

    def get(self, request):
        form = JournalForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            form = JournalForm()
            return redirect('history/')
        args = {'form': form}
        return render(request, self.template_name, args)

def index(request):
    all_journals = Journal.objects.all()
    return render(request, 'journal/index.html', {'all_journals': all_journals})


def detail(request, journal_id):
    try:
        journal = Journal.objects.get()
    except Journal.DoesNotExist:
        raise Http404("Journal Entry does not exist")
    return render(request, 'journal/details.html', {'journal': journal})
