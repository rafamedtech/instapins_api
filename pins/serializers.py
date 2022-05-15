from rest_framework import serializers
from .models import Comments, Pin, Like
from users.models import UserProfile
from users.serializers import UserProfileSerializer

class CommentsSerializer(serializers.ModelSerializer):
    username = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'username', 'email', 'comment', 'created_at', 'updated_at')

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('id',)

class PinSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
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
