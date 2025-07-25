from django.urls import path
from colortheory import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('sentiment_analysis/', views.sentiment_analysis, name='sentiment_analysis'),
    path('sentiment_palette/<str:sentiment>/', views.sentiment_palette, name='sentiment_palette'),
    path('artwork_creation/<str:sentiment>/', views.artwork_creation, name='artwork_creation'),
    path('analysis_tools/<str:sentiment>/', views.analysis_tools, name='analysis_tools'),
]
