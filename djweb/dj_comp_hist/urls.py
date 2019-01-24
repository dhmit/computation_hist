from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #re_path(r'person/(?P<person_id>).*', views.person, name='person'),
    path(r'person/<int:person_id>', views.person, name='person'),
    path('doc/<int:doc_id>', views.doc, name='document'),
    path('box/<int:box_id>', views.box, name='box'),
    #path('folder/<int:folder_id>', views.folder, name='folder'),

]