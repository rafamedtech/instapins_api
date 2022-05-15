from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .serializers import UploadSerializer
from .models import Upload

# Create your views here.

class UploadImage(APIView):

    parser_classes = [MultiPartParser, JSONParser, FormParser]
    serializer_class = UploadSerializer

    def get(self, request, *args, **kwargs):
        uploads = Upload.objects.all()
        serializer = UploadSerializer(uploads, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data

        upload = Upload.objects.create(
            image=data['image'],
            user=request.user
        )
        upload.save()

        serializer = self.serializer_class(upload)
        
        return Response(serializer.data, status=201)


class DeleteImage(APIView):

    def delete(self, request, pk, *args, **kwargs):
        image = Upload.objects.get(pk=pk)
        image.delete()

        return Response({'message': 'Image deleted'},status=204)