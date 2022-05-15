from rest_framework.serializers import ModelSerializer
from .models import ChatModel

class ChatModelSerializer(ModelSerializer):
    class Meta:
        model = ChatModel
        fields = ['sender', 'message', 'thread_name', 'timestamp']
        read_only_fields = ['timestamp']

    def create(self, validated_data):
        return ChatModel.objects.create(**validated_data)