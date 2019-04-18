from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from status.models import Status
from accounts.api.serializers import UserPublicSerializer


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # username = serializers.SlugRelatedField(source='user', read_only=True, slug_field='email')
    class Meta:
        model = Status
        fields = ('uri', 'id', 'user', 'summary', 'image')
        read_only_fields = ['user']

    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={"request": request}).data

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={"id": obj.id}, request=request)

    # def validate_content(self, value):
    #     if len(value) > 1000:
    #         raise serializers.ValidationError("This is way too long.")

    def validate(self, data):
        summary = data.get('summary', None)
        if summary == "":
            summary = None
        image = data.get("image", None)
        if ((summary is None) and (image is None)):
            raise serializers.ValidationError("Content or image is required.")
        return data


class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = ('uri', 'id', 'summary', 'image')

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=request)
