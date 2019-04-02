from django.shortcuts import render
from .models import Inspection


def index(request):
    inspection = Inspection()
    data = inspection.get_list()
    return render(request, 'blog/index.html', context={'data': data})
