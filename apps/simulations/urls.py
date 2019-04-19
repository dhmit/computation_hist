from django.urls import path

from . import views

urlpatterns = [
    path('punchcards/', views.punchcard_sim, name='punchcard_sim'),
    path('<str:simulation_name>', views.simulation, name="simulation"),
    path('', views.index_sim, name='index_sim')
]
