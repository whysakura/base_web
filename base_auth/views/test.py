# -*- coding: utf-8 -*-
# @Time    : 2017/6/2 11:54
# @Author  : wrd

from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.utils.encoding import smart_text
from django.db.models import Count, Q
from django.contrib.auth.models import User

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__file__)

class Index(View):
    # template_name = 'main/index.html'

    def get(self, request):
        data = {}
        logger.info('1111')
        logger.error('1111')
        return HttpResponse('l1kj23')
