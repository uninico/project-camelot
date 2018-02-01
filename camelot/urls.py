from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('home', views.user_home, name='user_home'),
]
