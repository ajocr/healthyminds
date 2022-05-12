from django.urls import path
from . import views
from journal import views

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('', views.index, name='home'),

    #path('', views.homecss, name='homecss'),
]
