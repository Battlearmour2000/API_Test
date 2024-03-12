from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.post_data),
    path('user_address/', views.get_Addressdata),
    path('add_userAddress/', views.post_Addressdata)
]