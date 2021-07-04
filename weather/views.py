import json
import urllib.request
import environ

from django.shortcuts import render

env = environ.Env()


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + env('OPEN_WEATHER_API_KEY')).read()
        json_data = json.loads(res)
        context = {
            'city': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',

        }
    else:
        context = {}
    return render(request, 'home.html', context)
