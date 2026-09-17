from django.urls import path
from . import views

urlpatterns = [
    path('', views.honeypot_view, name='honeypot'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/logs/', views.api_logs, name='api_logs'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
