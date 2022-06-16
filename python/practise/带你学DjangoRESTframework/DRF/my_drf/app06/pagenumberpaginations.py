from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from .custom_json_response import JsonResponse
from rest_framework import status


class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link(), count=self.page.paginator.count)

# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 1
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 2
#
#     def get_paginated_response(self, data):
#         return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
#                             previous=self.get_previous_link(), count=self.count)
#
#
# class MyPageNumberPagination(CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 1
#     ordering = 'id'
#     page_size_query_param = 'size'
#     max_page_size = 1
#
#     def get_paginated_response(self, data):
#         return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
#                             previous=self.get_previous_link())
