from django.urls import path

from . import views

app_name = 'others'
urlpatterns = [
    path('notfound/', views.notfound, name="notfound"),
   
]