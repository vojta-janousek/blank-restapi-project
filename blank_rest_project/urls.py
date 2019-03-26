"""blank_rest_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from updates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^json/example/$', views.json_example_view),
    re_path(r'^json/cbv/$', views.JsonCBV.as_view()),
    re_path(r'^json/cbv2/$', views.JsonCBV2.as_view()),
    re_path(r'^json/serialized/list/$', views.SerializedListView.as_view()),
    re_path(r'^json/detailed/list/$', views.SerializedDetailView.as_view()),
]
