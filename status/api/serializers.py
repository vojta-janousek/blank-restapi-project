from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'user', 'summary', 'image')
        read_only_fields = ['user']

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("This is way too long.")

    def validate(self, data):
        summary = data.get('summary', None)
        if summary == "":
            summary = None
        image = data.get("image", None)
        if ((summary is None) and (image is None)):
            raise serializers.ValidationError("Content or image is required.")
        return data
