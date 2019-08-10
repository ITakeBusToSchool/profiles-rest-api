from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSericalizer


    def get(self,request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get, post , path, put ,delete)',
            'is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self,requet,pk=None):
        """Hand updating an object"""
        return Response({'methods':'PUT'})

    def patch(self,request, pk=None):
        """Hand a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request, pk=None):
        return Response({'method':'DELETE'})
