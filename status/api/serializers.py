from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = ('uri', 'id', 'user', 'summary', 'image')
        read_only_fields = ['user']

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)

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
