from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mealmind'),
    path('mealmind/about/', views.about, name='about'),
    path('details/<slug:slug>/', views.details, name='recipe_details'),
    path('mealmind/food/', views.food, name='food'),
]
