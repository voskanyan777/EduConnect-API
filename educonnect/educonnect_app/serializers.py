from rest_framework import serializers


class CreateCourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90, allow_null=False)
    description = serializers.CharField(max_length=350, allow_null=True)
    available_groups = serializers.JSONField(allow_null=True, required=False)
