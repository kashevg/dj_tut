from django.shortcuts import render
from .models import Inspection


def index(request):
    inspection = Inspection()
    data = inspection.get_list()
    return render(request, 'blog/index.html', context={'data': data})


def details(request, id):
    inspection = Inspection()
    data = inspection.get_one(id)
    return render(request, 'blog/details.html', context={'data': data})
