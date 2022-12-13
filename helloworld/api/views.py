from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['GET'])
def getData(request):
    person = {'name':"John", 'age': 21}
    return Response(person)

@api_view(['POST'])
def postData(request):
    print("POST data: ", request.data)
    return Response("Thank you for POSTing")

class HelloWorld(APIView):
    def get(self, request):
        person = {'name':"Harry", 'age': 21}
        return Response(person)
    def post(self, request):
        print("POST data: ", request.data)
        return Response("Thank you for POSTing")