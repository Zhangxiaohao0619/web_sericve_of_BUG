#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import  render

def add(request):
    a = request.GET.get('a',1)
    b = request.GET.get('b',1)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    return HttpResponse("这是一个伟大的时代")

def home(request):
    return  render(request,"home.html")

def home2(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home2.html', {'string': string})

def home3(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home3.html', {'TutorialList': TutorialList})