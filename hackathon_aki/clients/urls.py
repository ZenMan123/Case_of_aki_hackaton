from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_client_profile, name='redirect_to_client_profile'),
    path('profile/', views.show_client_profile, name='show_client_profile'),
    path('registration/', views.registration, name='registration'),
]
