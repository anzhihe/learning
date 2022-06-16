from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

# Create your views here.
#
# class GameList(generics.ListCreateAPIView):
#     serializer_class = GameSerializer
#     queryset = Game.objects.filter().all()


# 版本过滤
# def get_queryset(self):
#     if self.request.version == 'v1':
#         queryset = Game.objects.filter(status=1).all()
#     else:
#         queryset = Game.objects.filter(status=0).all()
#     return queryset

# def get_serializer_class(self):


# class GameDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer


from .custom_generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class GameList(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.filter().all()


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


from rest_framework.parsers import FormParser, JSONParser, FileUploadParser, MultiPartParser

from rest_framework.views import APIView
from django.http import HttpResponse


class ParserView(APIView):
    # parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        # print("body:", request.body.decode())
        print("content_type:", request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print("data:", request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print("POST:", request.POST)
        print("FILES:", request.FILES)

        return HttpResponse('响应')


# ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# class GameViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer


from .custom_model_view_set import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filter import GameFilter
from rest_framework import filters


class GameViewSet(CustomModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    # 利用get_queryset 来实现过滤
    # def get_queryset(self):
    #     ordering = self.request.query_params.get('ordering')
    #
    #     if not ordering:
    #         queryset = Game.objects.all()
    #     else:
    #         queryset = Game.objects.order_by(ordering)
    #     return queryset

    # 过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 局部
    # filter_fields = ('name', 'status',"id")
    filterset_class = GameFilter

    # 搜索
    search_fields = ('name', 'status', 'id')

    # 支持排序的字段
    ordering_field = ('id', 'status')
