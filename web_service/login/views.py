#coding=UTF-8

from django.http import HttpResponse
from django.shortcuts import  render

import json


def login(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '张小浩'}

    return render(request, 'login.html',{'List': json.dumps(List),'Dict': json.dumps(Dict)})



