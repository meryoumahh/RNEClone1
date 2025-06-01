from django.shortcuts import render

def home(request):
    return render(request, 'rneClone/home.html')

def simulateur(request):
    return render(request, 'rneClone/SimulateurDenomination.html')

def Chatter(request):
    return render(request, 'rneClone/Chatbot.html')
