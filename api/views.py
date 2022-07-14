from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GetRoutes(APIView):
    def get(self, request):

        routes = [
            
            {'POST':'/pins/'},

            {'GET':'/pins/details/<id>/'},
            {'GET':'/pins/details/<id>/edit/'},
            {'POST':'/pins/create/'},
            {'DELETE':'/pins/delete/'},

            {'POST':'/pins/comment/<str:id>/'},
            {'DELETE':'/pins/comment/<str:id>/<str:pk>/'},
            {'POST':'/pins/like/<str:id>/'},

            {'GET':'/users/user/'},
            {'POST':'/users/register/'},
            {'POST':'/users/token/'},
            {'POST':'/users/logout/'},
            

        ]

        return Response(routes)

        