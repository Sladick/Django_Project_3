from django.shortcuts import render, get_object_or_404
import requests
from .models import City
from .forms import CityForm
from django.views.generic import DeleteView


def get_weather(request):
    appid = '22d6ecb88a99cf1a366aab3e95420aef'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if(request.method =='POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()


    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'loli': city.id

        }
        all_cities.append(city_info)


    context = {'all_info': all_cities, 'form': form, 'cities': cities}

    return render(request, 'weather/get_weather.html', context)


class Delete_weather(DeleteView):
    model = City
    template_name = 'weather/delete_weather.html'
    success_url = '/weather/'
    context_object_name = 'article'


def get_weather(request):
    appid = '22d6ecb88a99cf1a366aab3e95420aef'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'id': city.id

        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form, 'cities': cities}

    return render(request, 'weather/get_weather.html', context)




