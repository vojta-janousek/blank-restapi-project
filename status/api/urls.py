from django.urls import path, re_path
from status.api import views

urlpatterns = [
    re_path(r'^create/$', views.StatusCreateAPIView.as_view()),
    #re_path(r'^(?P<id>.*)/$', views.StatusDetailAPIView.as_view()),
    #re_path(r'^(?P<id>.*)/update/$', views.StatusUpdateAPIView.as_view()),
    #re_path(r'^(?P<id>.*)/delete/$', views.StatusDeleteAPIView.as_view()),
    re_path(r'^$', views.StatusAPIView.as_view()),
]
