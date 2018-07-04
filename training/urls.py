from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('calendar', views.calendar, name='calendar'),
    path('<slug:slug>/', views.TrainingView.as_view(), name='traininghome'),
]