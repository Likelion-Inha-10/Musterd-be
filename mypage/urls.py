from django.urls import path
from mypage import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('promise_place/<int:plan_id>',views.promise.as_view()),
    path('finish/<int:plan_id>',views.promise.as_view()),
    path('delete/<int:plan_id>',views.promise.as_view()),
    path('create/plan',views.promise.as_view()),
    path('',views.PlanList.as_view()),
    path('fine/place', views.elec_location),
    
]