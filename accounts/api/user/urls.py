from django.urls import path, re_path

from accounts.api.user import views

app_name = 'accounts'
urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', views.UserDetailApiView.as_view(), name='detail'),
    re_path(r'^(?P<username>\w+)/status/$', views.UserStatusApiView.as_view(), name='status-list'),
]
