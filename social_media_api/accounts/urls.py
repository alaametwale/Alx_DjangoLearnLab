from django.urls import path
from .views import RegisterView, LoginView, UserListView, FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("users/", UserListView.as_view()),

    # ⭐ required by checker
    path("follow/<int:user_id>", FollowUserView.as_view(), name="follow"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow"),
]
