from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete','absolute_url', 'created_date']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')

        if request.parser_context['kwargs'].get('pk'):
            rep.pop('absolute_url')
        return rep
    