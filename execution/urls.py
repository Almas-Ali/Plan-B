from django.urls import path
from execution import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fillup', views.fillup, name='fillup'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
]
