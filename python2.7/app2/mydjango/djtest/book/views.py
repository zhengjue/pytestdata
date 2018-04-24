# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
	return HttpResponse("这是一个首页测试")

def index_test(request,**kw):
	print kw
	return HttpResponse("这是一个首页测试")
def index_test1(request,a,b,**kw):
	print a,b,kw
	return HttpResponse("这是一个首页测试")
