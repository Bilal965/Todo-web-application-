from django.contrib import admin
from django.urls import path,include
from todo import views
urlpatterns = [
    path('createtodo/', views.CreateTodo.as_view(),name="createtodo"),
    path('createtodo/<int:myid>/', views.RudTodo.as_view(),name="RUDTODO"),
    path('alltodo/', views.Alltodo.as_view(),name="Alltodo"),
]
