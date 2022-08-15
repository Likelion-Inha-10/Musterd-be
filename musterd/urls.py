from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('mypage/', include('mypage.urls')),
    path('friend/', include('friend.urls')),
    path('search/', include('search.urls')),
]