from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello world")


def simulation(request, sim_name):
    obj_dict = {
        "simulation_name": sim_name,
        "script_name": "/static/js/" + sim_name + ".js",
    }
    return render(request, sim_name + '.jinja2', obj_dict)


def index_sim(request):
    return render(request, 'index_sim.jinja2')
