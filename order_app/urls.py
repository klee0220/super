from django.urls import path, include
from . import views

urlpatterns = [
    #path('example/', views.example_view, name='example'),
    path('order/', include('order_app')),
]