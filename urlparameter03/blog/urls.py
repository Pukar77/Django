from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("user/<str:username>/", views.user_profile, name="User_profile")
]