from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from profiles import serializers

class HelloApiView(APIView):

    serializer_class = serializers.helloserializer

    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'Is Similar to a tradational Dajango View',
            'Gives you the most control over out application logic',
            'Is mapped manually to urls',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        return Response({'method':'patcht'})


    def delete(self,request,pk=None):
        return Response({'method':'delete'})


class Helloviewset(viewsets.ViewSet):
    serializer_class = serializers.helloserializer

    def list(self,request):
        a_viewset=[
            'Uses actions (list create,update, partial update)',
            'Maps urls using routers',
        ]
        return Response({'Message': 'Hello','a_viewset':a_viewset});

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})