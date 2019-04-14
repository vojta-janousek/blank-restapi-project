import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404

from .serializers import StatusSerializer
from status.models import Status
from accounts.api.permissions import IsOwnerOrReadOnly

# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIDetailView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusAPIView(
        mixins.CreateModelMixin,
        generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer
    # passed_id = None

    def get_queryset(self):
        print(self.request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(summary__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    #
    # def put(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #
    #     return self.destroy(request, *args, **kwargs)



# class StatusCreateAPIView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer



# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
