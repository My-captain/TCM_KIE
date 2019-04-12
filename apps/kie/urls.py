# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 13:07
# @Author  : Mr.Robot
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url, include
from django.urls import path, re_path
from .views import KIEView

urlpatterns = [
    re_path(r'^', KIEView.as_view(), name="kie"),
]

app_name = 'kie'
