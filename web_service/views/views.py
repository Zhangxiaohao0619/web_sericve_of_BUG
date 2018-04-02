#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import  render

from tools.forms import AddForm

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

def home4(request):
    dict_home4 = {"code" : 1 , "name" : "账号"}
    return render(request, 'home4.html' , {'dict_home4' : dict_home4})

def home5(request):
    dict_home5 = map(str,range(100))
    return  render(request,'home5.html' , {"dict_home5" : dict_home5})

def index(request):
    if request.method == 'POST':# 当提交表单时

        form = AddForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:# 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))