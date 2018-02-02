
from rest_framework.pagination import PageNumberPagination

class PageSizeNumberPagination(PageNumberPagination):
  page_size = 12
  page_size_query_param = "page_size"
  page_query_description = "分页大小"
  max_page_size = 20
