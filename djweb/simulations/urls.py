from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('<str:simulation>', views.simulation, name="simulation"),
]
