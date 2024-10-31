from rest_framework import serializers

from educonnect_app.models import Task


class CreateCourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90, allow_null=False)
    description = serializers.CharField(max_length=350, allow_null=True)
    available_groups = serializers.JSONField(allow_null=True, required=False)


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'for_course', 'deadline')

    def create(self, validated_data):
        user = self.context['request'].user
        task = Task(
            name=validated_data['name'],
            description=validated_data['description'],
            for_course=validated_data['for_course'],
            created_by_teacher=user,
            deadline=validated_data['deadline'],
        )
        task.save()
        return task


class CreateGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90)
