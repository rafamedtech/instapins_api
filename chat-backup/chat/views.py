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

        all_threads = ChatModel.objects.all()
        my_threads = []
        
        for thread in all_threads:
            me = request.user
            other = UserProfile.objects.get(username=thread.sender)
            
            if me.id > other.id:
                thread_name = f'chat_{me.id}_{other.id}'
            else:
                thread_name = f'chat_{other.id}_{me.id}'

            if thread.thread_name == thread_name:
                my_threads.append(thread)
            
            if thread.sender == request.user.username:
                my_threads.append(thread)



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