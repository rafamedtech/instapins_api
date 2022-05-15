from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


from pins.serializers import PinSerializer, CommentsSerializer, LikeSerializer
from .models import Comments, Pin, Like

# Create your views here.
class GetPins(APIView):

    serializer_class = PinSerializer

    def get(self, request, *args, **kwargs):
        pins = Pin.objects.all()
        serializer = self.serializer_class(pins, many=True)

        return Response(serializer.data, status=200)

class GetSinglePin(APIView):

    serializer_class = PinSerializer

    def get(self, request, pk, *args, **kwargs):
        pin = Pin.objects.get(pk=pk)
        serializer = self.serializer_class(pin)

        return Response(serializer.data, status=200)

class PostPin(APIView):

    parser_classes = [MultiPartParser, JSONParser, FormParser]
    serializer_class = PinSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        pin = Pin.objects.create(
            title=data['title'],
            description=data['description'],
            url=data['url'],
            owner=request.user
        )

        serializer = self.serializer_class(pin)
        return Response(serializer.data, status=201)

class updatePin(APIView):

    parser_classes = [MultiPartParser, JSONParser, FormParser]
    serializer_class = PinSerializer

    def put(self, request, pk, *args, **kwargs):
        data = request.data

        pin = Pin.objects.get(pk=pk)
        pin.title = data['title']
        pin.description = data['description']
        
        pin.save()

        serializer = self.serializer_class(pin)
        return Response(serializer.data, status=200)

class DeletePin(APIView):

    def delete(self, request, pk, *args, **kwargs):
        pin = Pin.objects.get(id=pk)
        pin.delete()

        return Response({'message': 'Pin deleted'},status=204)

class CommentPin(APIView):

    serializer_class = CommentsSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        
        pin = Pin.objects.get(id=data['pin'])
        comment = Comments.objects.create(
            username = request.user,
            email = request.user,
            comment = data['comment']
        )
        pin.comments.add(comment)

        serializer = self.serializer_class(comment)

        return Response(serializer.data, status=201)

class DeleteComment(APIView):

    def delete(self, request, pk, *args, **kwargs):
        comment = Comments.objects.get(pk=pk)
        comment.delete()

        return Response({'message': 'Comment deleted'},status=204)

class LikePin(APIView):

    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        

        # validate if user has already liked the pin
        if Like.objects.filter(pins=data['id'], username=request.user).exists():
            return Response({'message': 'You have already liked this pin'}, status=400)

        pin = Pin.objects.get(id=data['id'])
        
        like = Like.objects.create(
            username = request.user
        )
        pin.likes.add(like)

        serializer = self.serializer_class(like)

        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        data = request.data
        print(f"data: {data}")
        pin = Pin.objects.get(id=data['id'])
        like = Like.objects.get(pins=pin, username=request.user)
        like.delete()

        return Response({'message': 'Like deleted'},status=204)