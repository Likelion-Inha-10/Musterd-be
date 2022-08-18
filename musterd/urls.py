from django.contrib import admin
from django.urls import path,include
from account.views import TravelStampAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('mypage/', include('mypage.urls')),
    path('friend/', include('friend.urls')),
    path('search/', include('search.urls')),
    path('travel-stamp', TravelStampAPIView.as_view())
]