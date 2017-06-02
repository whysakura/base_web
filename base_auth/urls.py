# -*- coding: utf-8 -*-
# @Time    : 2017/6/2 11:50
# @Author  : wrd

from django.conf.urls import url
from base_auth.views import test

urlpatterns = [
    url(r'^$', test.Index.as_view(), name='index'),
]