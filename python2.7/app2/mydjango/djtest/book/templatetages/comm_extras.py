#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 
# @Author  :  ()
# @Link    : 
# @Version : $Id\$
import datetime
from django import template
register = template.Library()

# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def current_time(context):
    tstr=context['format_string']
    return datetime.datetime.now().strftime(tstr)

@register.inclusion_tag("book/list_tag.html")
def show_list():
    li=['python','c++','java']
    return {"List":li}



if __name__ == '__main__':
    pass
