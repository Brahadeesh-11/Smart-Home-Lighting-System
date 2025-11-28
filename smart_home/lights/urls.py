from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toggle/<str:light_id>/', views.toggle_light, name='toggle_light'),
]
