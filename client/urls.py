from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name='home'),
]
