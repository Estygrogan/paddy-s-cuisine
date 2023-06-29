from django.shortcuts import render
from datetime import datetime
from .models import booking

def base(request):
    return render(request, "base.html", {})