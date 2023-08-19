from django.shortcuts import render
from .models import Service
# Create your views here.
# def services(request):
#     return render(request, "services/services.html")projects=Proyect.objects.all()
def services(request):
    services=Service.objects.all()
    return render(request, "services/services.html", {'services': services})  