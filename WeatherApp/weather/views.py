from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityFrom

def index(request):
    appid = '3dd9b7a8647d9aaa0244b7fa9748f909'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    cities = City.objects.all()
    all_cities = []
    if request.POST:
        if 'send' in request.POST:
            res = requests.get(url.format(request.POST['name'])).json()
            if res['cod'] == '404':
                form = []
            else:
                form = CityFrom(request.POST)
                form.save()
    form = CityFrom
    for city in cities:
        res = requests.get(url.format(city)).json()
        if res['cod'] == '404':
            continue
        else:
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'id': city.id
            }
            all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}


    return render(request, 'weather/index.html', context=context)

def delete(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()

    return redirect('home')

def about(request):
    return render(request, 'weather/about.html')