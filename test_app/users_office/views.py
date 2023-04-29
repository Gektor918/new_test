from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status

from users_office.models import *
from .serializers import *


class UserListView(ListAPIView):

    """
    Listing all users and their associated organizations
    """

    def get(self, requset):

        queryset_user = User.objects.all()
        serializer_class = UserSerializer(queryset_user, many=True)

        need_info = [(i['email'], list(set(i['office']))) for i in serializer_class.data]
        user_and_office = ()

        for i in need_info:
            list_office = [Office.objects.get(id=x).name for x in (i[1])]
            user_and_office += (i[0],list_office)
            
        return Response({'user_and_office': user_and_office,
                        'user_all_info': serializer_class.data})


class UserOne(APIView):

    """
    Output of one user by his ID, with a list of organizations associated with him
    """

    def post(self, request):

        try:
            queryset_user = User.objects.get(id = request.data.get('id'))
            serializer_class = UserSerializer(queryset_user)
        except:
            return Response('Неверный id', status=status.HTTP_204_NO_CONTENT)
    
        list_office = [Office.objects.get(id=i).name for i in set(serializer_class.data.get('office'))]

        return Response({'serializer_class':serializer_class.data, 
                        'list_office':list_office},
                        status=status.HTTP_200_OK)


class RegistrUserView(CreateAPIView):

    """
    Creating a new user (registration)
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = UserRegistrSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data['response'] = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserUpdate(APIView):

    """
    Editing your profile (changing data in your profile)
    """

    def put(self,request):

        try:
            profile_user = User.objects.get(email = request.data.get('email'))
        except:
            return Response('Укажите email')

        serializer = UserUpdateSerializer(data=request.data, instance=profile_user)
        data = {}

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['response'] = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class AddNewOffice(APIView):

    """
    Adding a new organization
    """

    def post(self,request):

        serializer = OfficeSerializer(data = request.data)
        data = {}

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['response'] = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class OfficeAll(ListAPIView):

    """
    Displaying a list of all organizations
    """

    def get(self, requset):
        queryset_office = Office.objects.all()
        serializer_class = OfficeSerializer(queryset_office, many=True)
        return Response({"all_office":serializer_class.data}, status=status.HTTP_200_OK)