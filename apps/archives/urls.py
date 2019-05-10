from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<str:slug>', views.person, name='person'),
    path('doc/<str:slug>', views.doc, name='document'),
    path('search/', views.search, name='search'),
    path('box/<str:slug>', views.box, name='box'),
    path('folder/<str:slug>', views.folder, name='folder'),
    path('organization/<str:slug>', views.organization, name='organization'),
    path('list/<str:model_str>', views.list_obj, name='list'),
    path('browse/', views.browse, name='browse'),
    path('story/<str:slug>', views.story, name='story'),
    path('timeline/', views.timeline, name='timeline'),
    path('net_viz', views.net_viz, name='net_viz'),
    path('stories/', views.stories, name='stories'),
    path('our_team/', views.our_team, name='our_team'),
    path('all_docs/', views.all_docs) # for metadata checking
]
