from django.urls import path
from main import views

urlpatterns = [
    path('',views.index),
    path('addtodo/',views.addtodo),
    path('deletetodo/<int:pk>/',views.deletetodo)
]
