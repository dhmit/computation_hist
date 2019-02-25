from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello world")


def simulation(request):
    obj_dict = {}
    return render(request, 'assembly_addition.jinja2', obj_dict)
