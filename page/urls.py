from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page-detail'),
    path('pages/about-us/', views.AboutView.as_view(), name='page-about'),
]
