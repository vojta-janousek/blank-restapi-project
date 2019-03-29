from django.urls import path, re_path

urlpatterns = [
    re_path(r'^create/$', StatusCreateAPIView.as_view()),
    re_path(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    re_path(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    re_path(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
    re_path(r'^$', StatusListSearchAPIView.as_view()),
]
