from django.urls import path
from .import views

# app_name = 'home'

urlpatterns = [

    path("", views.home, name="home"),
    path("list/", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<category>/", views.category, name="category"),
   
]
