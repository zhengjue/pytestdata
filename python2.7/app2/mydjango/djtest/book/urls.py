"""djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    #url(r'^(\w+)/(\d+)/(?P<bname>\w+)', views.index_test,name="pythonurl",{"k":"vtest"}),
    url(r'^(?P<bname>\w+)/$', views.index_test,{"k":"vtest"},name="pythonurl"),
    url(r'^(\w+)/(\d+)/$', views.index_test1,{"k":"vtest"},name="pythonurl1"),
]
