from django.urls import path
from . import views
from moodtracker_.views import MoodtrackerView

urlpatterns = [
    # /moodtracker/
    path('', MoodtrackerView.as_view(), name='enter'),

    # /moodtracker/71/
    path("<int:moodtracker_id>/", views.detail, name='detail'),

    path("history/", views.index, name='history'),
]
