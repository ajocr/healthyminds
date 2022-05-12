from django.urls import path
from . import views
from journal.views import JournalView

urlpatterns = [
    # /journal/
    path('', JournalView.as_view(), name='enter'),

    # /journal/71/
    path("<int:journal_id>/", views.detail, name='detail'),

    path("history/", views.index, name='history'),
]