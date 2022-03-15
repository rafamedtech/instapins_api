from rest_framework import serializers
from uploads.models import Upload

class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        upload = Upload.objects.create(**validated_data)
        return upload
