from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, get_list_or_404

def test(request):
    return HttpResponse("Hello world")


def simulation(request, simulation):
    obj_dict = {
        "simulation_name": simulation,
        "script_name": "/static/js/" + simulation + ".js",
    }
    return render(request, simulation + '.jinja2', obj_dict)


def index_sim(request):
    return render(request, 'index_sim.jinja2')
