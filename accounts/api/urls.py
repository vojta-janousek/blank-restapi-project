from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from accounts.api import views

urlpatterns = [
    re_path(r'^jwt/$', obtain_jwt_token),
    re_path(r'^jwt/refresh/$', refresh_jwt_token),
    re_path(r'^$', views.AuthAPIView.as_view()),
    re_path(r'^register/$', views.RegisterAPIView.as_view()),
]
