from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles import permissions
from profiles import serializers
from profiles import models

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

class Userprofileviewset(viewsets.ModelViewSet):
    serializer_class = serializers.userprofileserializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateownprofile,)
    filter_backends=(filters.SearchFilter,)
    search_fields = ('name','email',)

class Userloginapiview(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class userprofileviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.userprofileserializer
    query_set = models.profilefeeditem.objects.all()
    permission_class = (permissions.updateownstatus,
    IsAuthenticated)


    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)