from rest_framework import serializers
from .models import Comments, Pin, Like

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'name', 'email', 'comment', 'created_at', 'updated_at')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('id',)

class PinSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.name')
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        comments = validated_data.pop('comments')
        likes = validated_data.pop('likes')
        pin = Pin.objects.create(**validated_data)
        for comment in comments:
            Comments.objects.create(pin=pin, **comment)
        for like in likes:
            Like.objects.create(pin=pin, **like)
        return pin
