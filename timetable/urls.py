from django.urls import path
from . import views

urlpatterns = [
    path('monday', views.monday),
    path('tuesday', views.tuesday),
    path('wednesday', views.wednesday),
    path('thursday', views.thursday),
    path('friday', views.friday),
    path('saturday', views.saturday),
    path('sunday', views.sunday),
    path('1', views.monday),
    path('2', views.tuesday),
    path('3', views.wednesday),
    path('4', views.thursday),
    path('5', views.friday),
    path('6', views.saturday),
    path('7', views.sunday)
]