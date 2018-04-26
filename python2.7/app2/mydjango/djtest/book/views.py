# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
# def index(request):
#     return HttpResponse("这是一个首页测试")



def hello():
    return 'django'

class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        return 'HAHAHAHA'

ap = Fruits('apple', 'red')
ls = ['x', 'y', 'z']
dc = {'a': 1, 'b': 2}

from datetime import datetime
def index(request, **kw):
    return render(request, 'book/index.html',
                  context={'books_name': 'python',  # 字符串
                           'hello': hello,  # 函数
                           'fruits_say': ap.say,  # 方法
                           'fruits': ap,  # 类对象
                           'list': ls,  # 列表
                           'dict': dc,  # 字典
                           'test':"PYTHON TEST STRING",
                           'num1':1,
                           'num2':3,
                            'x1':None,
                            'x2':'',
                            'float':3.1415926,
                           'now':datetime.now(),
                           'html':"<h1>这是一个测试</h1>",
                           'text':"test test tset",
                           'text1':123,
                           'format_time':"%Y/%m/%d %H:%M:%S",
                           })



def index_test(request, **kw):
    return render("book/index.html",context={
        "dc":{"a":1,"b":2,"c":3}
    })

def index_test1(request, a, b, **kw):
    print a, b, kw
    return HttpResponse("这是一个首页测试")