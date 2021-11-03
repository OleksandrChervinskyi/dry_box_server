from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'data': data
        })
