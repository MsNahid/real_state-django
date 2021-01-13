from django.urls import path

from .import views

app_name = 'realtors'
urlpatterns =[
    path('<int:realtors_id>', views.profile, name="profile"),

]