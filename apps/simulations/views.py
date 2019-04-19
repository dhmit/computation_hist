from django.shortcuts import render
from django.http import HttpResponse

def simulation(request, simulation_name):
    obj_dict = {
        "simulation_name": simulation_name,
    }
    template = 'simulations/' + simulation_name + '.jinja2'
    return render(request, template, obj_dict)

def index_sim(request):
    return render(request, 'simulations/index.jinja2')

def punchcard_sim(request):
    return render(request, 'simulations/punchcards.jinja2')
