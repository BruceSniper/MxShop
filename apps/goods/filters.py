#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gt')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lt')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']