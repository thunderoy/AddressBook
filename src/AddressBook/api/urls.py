from django.urls import path, include, re_path
from .views import CreateContactApiView

urlpatterns = [
    path('create/', CreateContactApiView.as_view()),
]