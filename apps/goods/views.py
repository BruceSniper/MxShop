from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import GoodsSerializer
from .models import Goods
from .filters import GoodsFilter

# Create your views here.


# class GoodsListView(APIView):
#     """
#     List all goods
#     """
#     def get(self, request, format=None):
#         """
#         :param request:
#         :param format:
#         :return:
#         """
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

# def post(self, request, format=None):
#     serializer = GoodsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsPagination(PageNumberPagination):
    """
    商品列表页分页功能
    """
    page_size = 10
    # page_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
# # class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页搜索，过滤，排序 功能
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ("name", "goods_brief", "goods_desc")
    ordering_fields = ['sold_num', 'add_time']

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price=int(price_min))
    #     return queryset
