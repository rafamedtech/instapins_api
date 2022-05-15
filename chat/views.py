from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatModel
from users.models import UserProfile
from .serializers import ChatModelSerializer

# Create your views here.
class MessageAPIView(APIView):
    def get(self, request):
        # get all messages
        messages = ChatModel.objects.all()
        serializer = ChatModelSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleMessageAPIView(APIView):
    def get(self, request, username):
        user_obj = UserProfile.objects.get(username=username)
        users = UserProfile.objects.exclude(username=request.user.username)

        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'
        message_objs = ChatModel.objects.filter(thread_name=thread_name)