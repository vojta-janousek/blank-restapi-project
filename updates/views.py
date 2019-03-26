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
