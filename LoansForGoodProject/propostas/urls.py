from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('registro' ,views.paginainicial),
    path('api/v1/loan/', views.avaliar_proposta, name='avaliar_proposta'),
]
