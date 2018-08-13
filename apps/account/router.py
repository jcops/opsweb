#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Eric
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# register的可选参数 base_name: 用来生成urls名字，如果viewset中没有包含queryset, base_name一定要有
account_router = DefaultRouter()
account_router.register(r'users', UserViewSet, base_name='userviewset')