from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    path('homepage/', views.user_page),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('create/', views.create),
    path('contacts/', views.show),
    path('contacts/<contact_id>/', views.edit),
    path('contacts/<contact_id>/delete', views.delete),
]