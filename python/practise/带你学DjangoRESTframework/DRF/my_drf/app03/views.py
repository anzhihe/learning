from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import Http404


# Create your views here.


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# def user_list(request):
#     if request.method == 'GET':
#         user = User.objects.all()
#         ser = UserSerializer(instance=user, many=True, context={'request': request})
#         return JSONResponse(ser.data, content_type='application/json', status=200)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)  # 把前端传过来的json数据转成python里面数据类型
#
#         ser = UserSerializer(data=data, context={'request': request})
#
#         if ser.is_valid():
#             ser.save()
#             return JSONResponse(ser.data, content_type='application/json', status=201)
#
#         return JSONResponse(ser.errors, content_type='application/json', status=400)

#
# @api_view(['GET', 'POST'])
# def user_list(request):
#     if request.method == 'GET':
#         user = User.objects.all()
#         ser = UserSerializer(instance=user, many=True, context={'request': request})
#         return Response(ser.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#
#         ser = UserSerializer(data=request.data, context={'request': request})
#         if ser.is_valid(raise_exception=True):
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#

#

#
#
# @csrf_exempt
# def user_detail(request, id):
#     try:
#         user = User.objects.get(pk=id)
#     except User.DoesNotExist as e:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         ser = UserSerializer(instance=user, context={'request': request})
#         return JSONResponse(ser.data, status=200)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         ser = UserSerializer(instance=user, data=data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return JSONResponse(ser.data, status=201)
#         return JSONResponse(ser.errors, status=400)
#     elif request.method == 'PATCH':
#         data = JSONParser().parse(request)
#         ser = UserSerializer(instance=user, data=data, partial=True, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return JSONResponse(ser.data, status=201)
#         return JSONResponse(ser.errors, status=400)
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)


# class UserDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             user = User.objects.get(pk=pk)
#             return user
#         except Exception as e:
#             raise Http404()
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object(kwargs.get('pk'))
#         ser = UserSerializer(instance=user, context={'request': request})
#         return Response(ser.data, status=status.HTTP_200_OK)
#
#          自定义返回数据结构，在后面的讲
#         return JsonResponse(ser.data, code=200,msg='ok')
#
#     def put(self, request, *args, **kwargs):
#         user = self.get_object(kwargs.get('pk'))
#         ser = UserSerializer(instance=user, data=request.data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, *args, **kwargs):
#         user = self.get_object(kwargs.get('pk'))
#         ser = UserSerializer(instance=user, data=request.data, context={'request': request}, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         user = self.get_object(kwargs.get('pk'))
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import mixins
from rest_framework import generics

#
# class UserList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *arg, **kwargs):
#         return self.list(request, *arg, **kwargs)
#
#     def post(self, request, *arg, **kwargs):
#         return self.create(request, *arg, **kwargs)
#
#
# class UserDetail(mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# def patch(self, request, *args, **kwargs):
#     kwargs['partial'] = True
#     return self.update(request, *args, **kwargs)

# def patch(self, request, *args, **kwargs):
#     return self.partial_update(request, *args, **kwargs)
#
# def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)


# 通用的类视图

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
