from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GetRoutes(APIView):
    def get(self, request):

        routes = [
            
            {'POST':'/uploads/'},

            {'GET':'/uploads/<id>/'},
            

        ]

        return Response(routes)

        