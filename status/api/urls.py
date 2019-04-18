from django.urls import path, re_path
from status.api import views


app_name = 'status'
urlpatterns = [
    # re_path(r'^create/$', views.StatusCreateAPIView.as_view()),
    # re_path(r'^(?P<pk>\d+)/$', views.StatusDetailAPIView.as_view()),
    # re_path(r'^(?P<pk>\d+)/update/$', views.StatusUpdateAPIView.as_view()),
    # re_path(r'^(?P<pk>\d+)/delete/$', views.StatusDeleteAPIView.as_view()),
    re_path(r'^$', views.StatusAPIView.as_view()),
    re_path(r'^(?P<id>\d+)/$', views.StatusAPIDetailView.as_view(), name='detail'),
]
