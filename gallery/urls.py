from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryView.as_view(), name='galleryhome'),
]
