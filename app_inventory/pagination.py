from rest_framework.pagination import PageNumberPagination


class MaterialPagination(PageNumberPagination):
    page_size = 40
    max_page_size = 100


class InstrumentPagination(PageNumberPagination):
    page_size = 40
    max_page_size = 100
