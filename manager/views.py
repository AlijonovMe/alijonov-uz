from django.shortcuts import render
from .models import *
from datetime import datetime


def index(request):
    data = Database.objects.all()

    context = {
        'database': data,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)
