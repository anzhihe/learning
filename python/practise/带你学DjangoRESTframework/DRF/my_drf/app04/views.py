from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
from rest_framework import permissions
from .permissions import IsOwnOrReadOnly



# Create your views here.

# 通用的类视图

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # 到底给request.user赋值的


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnOrReadOnly]


