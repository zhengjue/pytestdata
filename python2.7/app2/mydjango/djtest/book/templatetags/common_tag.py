#!/usr/bin/env /python
# -*- coding:utf-8 -*-
# Author:Lza
import datetime
from django import template

register = template.Library()


# 简单自定义标签
@register.filter
def mycut(value, arg):
    return value.replace(" ", arg)

from django.template.defaultfilters import stringfilter
@register.filter
@stringfilter #变成字符串
def mylower(value):
    return value.lower()
#定义标签
@register.simple_tag
def current_now(format_time):
    return datetime.datetime.now().strftime(format_time)

#定义上下文标签
@register.simple_tag(takes_context=True)
def current_now1(context):
    return datetime.datetime.now().strftime(context["format_time"])

#包含标签（就是一段常用模板字段 作为一个标签）
@register.inclusion_tag("book/list_tag.html")
def show_list(arg):
    #l=["python","c++","java"]
    l=arg
    return {"List":l}

@register.inclusion_tag("book/list_tag.html",takes_context=True)
def show_list1(context):
    #l=["python","c++","java"]
    # l=arg
    return {"List":context["list"]}

#分配标签（就是标签去保存另一个另一个标签的结果）
@register.assignment_tag
def current_now2(format_time):
    return datetime.datetime.now().strftime(format_time)