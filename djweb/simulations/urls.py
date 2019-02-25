from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('assembler_test', views.simulation, name="simulation"),
]
