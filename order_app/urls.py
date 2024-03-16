# urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('create_request/', views.create_request, name='create_request'),
    path('update_request_status/<int:request_id>/', views.update_request_status, name='update_request_status'),
    path('complete_request/<int:request_id>/', views.complete_request, name='complete_request'),
    path('view_all_requests/', views.view_all_requests, name='view_all_requests'),
    # Добавляем путь для URL /order/
    path('', views.order_home, name='order_home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('request_detail/<int:request_id>/', views.request_detail, name='request_detail'),
]


