from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_phone, name='track_phone'),
    path('success/', views.tracking_success, name='tracking_success'),
]
