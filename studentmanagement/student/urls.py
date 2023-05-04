from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name= 'edit'),
]
