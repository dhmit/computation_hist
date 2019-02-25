from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello world")


def simulation(request):
    obj_dict = {}
    return render(request, 'assembler-test.jinja2', obj_dict)
