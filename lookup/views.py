#! Python 3
from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=48059&distance=100&API_KEY=146057C6-45D9-4C56-BF86-253216A93628")

    try:
        api = json.loads(api_request.content)   # call json and load up the content from api_request

    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
