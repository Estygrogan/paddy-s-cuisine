from django.shortcuts import render
from datetime import datetime
from .models import booking

def index(request):
    return render(request, "index.html", {})