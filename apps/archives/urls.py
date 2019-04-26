from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<str:slug>', views.person, name='person'),
    path('doc/<int:doc_id>', views.doc, name='document'),
    path('doc/<str:slug>', views.doc, name='document'),
    path('box/<str:slug>', views.box, name='box'),
    path('folder/<str:slug>', views.folder, name='folder'),
    path('organization/<str:slug>', views.organization, name='organization'),
    path('search_results/', views.search_results, name='search_results'),
    path('advanced_search/', views.advanced_search, name='advanced_search'),
    # Todo: Slugify at a much later time?
    path('list/<str:model_str>', views.list_obj, name='list'),
    path('browse/', views.browse, name='browse'),
    path('story/<str:slug>', views.story, name='story')
]
