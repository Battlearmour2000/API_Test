from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.post_data),
    path('user_address/', views.get_address_data),
    path('add_user_address/', views.post_address_data),
    path('get_address/<int:user_id>/', views.get_specific_user__address),
]