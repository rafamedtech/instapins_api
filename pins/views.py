from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from pins.serializers import PinSerializer, CommentsSerializer
from .models import Comments, Pin

# Create your views here.
class GetPins(APIView):

    serializer_class = PinSerializer

    def get(self, request, *args, **kwargs):
        pins = Pin.objects.all()
        serializer = self.serializer_class(pins, many=True)

        return Response(serializer.data, status=200)

class GetSinglePin(APIView):
    def get(self, request, pk, *args, **kwargs):
        pin = Pin.objects.get(pk=pk)
        serializer = PinSerializer(pin)

        return Response(serializer.data, status=200)

class PostPin(APIView):

    parser_classes = [MultiPartParser, JSONParser, FormParser]
    serializer_class = PinSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        pin = Pin.objects.create(
            label=data['label'],
            description=data['description'],
            url=data['url'],
            owner=request.user
        )

        serializer = self.serializer_class(pin)
        return Response(serializer.data, status=201)

class DeletePin(APIView):

    def delete(self, request, pk, *args, **kwargs):
        pin = Pin.objects.get(pk=pk)
        pin.delete()

        return Response({'message': 'Pin deleted'},status=204)

class CommentPin(APIView):

    serializer_class = CommentsSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.user)
        pin = Pin.objects.get(id=data['id'])
        comment = Comments.objects.create(
            name = data['name'],
            email = data['email'],
            comment = data['comment']
        )
        pin.comments.add(comment)

        serializer = self.serializer_class(comment)

        return Response(serializer.data, status=201)