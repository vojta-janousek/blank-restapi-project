import json

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from django.views.generic import View

from updates.models import Update
from blank_rest_project.mixins import JsonResponseMixin

# Create your views here.
def json_example_view(request):
    '''
    URI for a REST API
    GET -- Retrieve
    '''
    data = {
        "count": 1000,
        "content": "Some content"
    }
    return JsonResponse(data)


class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            "user": obj.user.username,
            "content": obj.content
        }

        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):

    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
