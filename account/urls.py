from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account import views
urlpatterns = [
    path("signup", views.RegisterAPIView.as_view()), 
    path("signin", views.AuthView.as_view()), 
    path("signout", views.logout.as_view()), 
  
]