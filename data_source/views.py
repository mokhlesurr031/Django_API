from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer, GroupSerializer, EmployeeSerializer
from .models import Employee

from rest_framework import viewsets, permissions
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer


def index(request):
    return HttpResponse("Hello")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    print(queryset)
    serializer_class = EmployeeSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)


