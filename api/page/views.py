from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import NP
from .serializers import NPSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Index(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if "Title" in request.GET:
            np = NP.objects.filter(Title__icontains = request.GET["Title"])
        elif "id" in request.GET:
            np = NP.objects.filter(id = request.GET['id'])
        else:
            np = NP.objects.order_by("-id")
        serializer = NPSerializer(np, many=True)
        return Response(serializer.data)

class Create(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if not request.data._mutable:
            request.data_mutable = True
        request.data["User"] = str(request.user.username)
        serializer = NPSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 201})
        return Response(serializer.errors)

class Signup(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        if username is None and password is None:
            return Response({"status": 400})
        try:
            User.objects.create_user(username = username, password = password).save()
            return Response({"status": 201})
        except IntegrityError:
            return Response({"status": 400})