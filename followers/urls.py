from django.urls import path
from followers import views

urlpatterns = [
    path('follows/', views.FollowList.as_view()),
    path('follows/<int:pk>', views.FollowDetail.as_view()),
]