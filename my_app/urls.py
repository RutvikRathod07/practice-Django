from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_home_page),
    path('home/', views.show_home_page),
    path('about/', views.about_page),
    path('service/', views.service_page),
    path('info/', views.info_page),
    path('add/', views.add,name='add'),
]




















