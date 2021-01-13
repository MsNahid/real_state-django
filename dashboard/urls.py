from django.urls import path

from .import views

app_name = 'dashboard'
urlpatterns =[
    path('', views.dash, name="dash"),
    path('create_realtors',  views.create_realtors, name="create_realtors"),
    path('update_property/<str:pk>/',  views.update_property, name="update_property"),
    path('delete_property/<str:pk>/',  views.delete_property, name="delete_property"),

]