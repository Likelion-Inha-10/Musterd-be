from django.urls import path
from mypage import views
from django.views.decorators.csrf import csrf_exempt
from friend.views import listPlans
from friend import views
urlpatterns = [
    path('plan', views.listPlans.as_view()),
]