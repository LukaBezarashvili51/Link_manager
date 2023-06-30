from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.link_create, name='link_create'),
    path('update/<int:pk>/', views.link_update, name='link_update'),
    path('delete/<int:pk>/', views.link_delete, name='link_delete'),
    path('', views.link_list, name='link_list'),
]
