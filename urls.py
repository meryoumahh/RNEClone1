from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SimulateurDenomination.html', views.simulateur, name='simulateur'),
     path('Chatbot.html', views.Chatter, name='ChatBot')
]