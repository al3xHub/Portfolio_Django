from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio(request):
    projects = Project.objects.all()  # Nos devuelve toda la lista de proyectos creados.
    return render(request, "portfolio/portfolio.html", {'projects': projects})
