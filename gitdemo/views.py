#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/7 13:40

from django.http import HttpResponse


def index_view(request):
    return HttpResponse('Hello git')
