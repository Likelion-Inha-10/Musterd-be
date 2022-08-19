from django.urls import path
from friend import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create',views.join),
    path('rank',views.RankList.as_view()),
    path('plan/<int:friend_id>', views.listPlans.as_view()),
    
]

