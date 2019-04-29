from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'person/<int:person_id>', views.person, name='person'),
    path('doc/<str:slug>', views.doc, name='document'),
    path('box/<int:box_id>', views.box, name='box'),
    path('folder/<int:folder_id>', views.folder, name='folder'),
    path('organization/<int:org_id>', views.organization, name='organization'),
    path('search/', views.advanced_search, name='advanced_search'),
    path('list/<str:model_str>', views.list_obj, name='list'),
    path('page/<int:page_id>', views.page, name='page'),
    path('browse/', views.browse, name='browse'),
    path('story/<str:slug>', views.story, name='story'),
    path('net_viz', views.net_viz, name='net_viz'),
    path('stories/', views.stories, name='stories')
]
