from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serialize a task"""

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'description', 'time_required', 'start_date',
            'updated_on', 'comment'
        )
        read_only_fields = ('id', 'start_date', 'updated_on', 'comment')


#
class TaskCommentSerializer(serializers.ModelSerializer):
    """Serializer for commenting task"""

    class Meta:
        model = Task
        fields = ('id', 'comment', 'name', 'description', 'time_required', 'start_date')
        read_only_fields = ('id', 'name', 'description', 'time_required', 'start_date')
