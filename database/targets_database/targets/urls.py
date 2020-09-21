from django.urls import path
from targets import views

urlpatterns = [
    path('targets/',views.TargetList.as_view()),
    path('targets/<int:pk>/', views.target_detail),
    path('targetgroups/', views.targetgroup_list),
]