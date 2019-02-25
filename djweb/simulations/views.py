from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, get_list_or_404

def test(request):
    return HttpResponse("Hello world")


def simulation(request, simulation):
    # simulation_obj = get_object_or_404(Simulation, pk=simulation)
    obj_dict = {
        # "simulation-name": simulation_obj,
    }
    return render(request, simulation + '.jinja2', obj_dict)
