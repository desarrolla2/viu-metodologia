from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulate', views.simulate, name='simulate'),
    path('random', views.random, name='random'),
    path('clear', views.clear, name='clear'),
    path('orchid/create', views.orchid_create, name='orchid_create'),
    path('orchid/list', views.orchid_list, name='orchid_list'),
    path('greenhouse/create', views.greenhouse_create, name='greenhouse_create'),
    path('greenhouse/list', views.greenhouse_list, name='greenhouse_list'),
]
