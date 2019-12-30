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
        np = NP.objects.order_by("-id")
        serializer = NPSerializer(np, many=True)
        return Response(serializer.data)