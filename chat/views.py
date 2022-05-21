from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import UserProfile
from .models import ChatModel
from users.serializers import UserProfileSerializer
from .serializers import ChatModelSerializer

# Create your views here.
class MessageAPIView(APIView):
    def get(self, request):

        my_threads = []


        for thread in ChatModel.objects.all():
            user = UserProfile.objects.get(username=thread.sender)
            if request.user == user:
                my_threads.append(user)
                if user.id > request.user.id:
                    thread_name = f'chat_{user.id}-{request.user.id}'
                else:
                    thread_name = f'chat_{request.user.id}-{user.id}'

            else:
                threads = ChatModel.objects.get(thread_name=thread_name)
                my_threads.append(threads)


        serializer = ChatModelSerializer(my_threads, many=True)

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