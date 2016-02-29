#coding:utf-8
from django.shortcuts import render,render_to_response
from Blog.models import *
from django.http import Http404
from django.conf import settings
import datetime
#分页
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    limit=10     #每页显示的记录数
    tags=Tag.objects.all()
    blog_list=Blog.objects.all()
    paginator=Paginator(blog_list,limit)
    page = request.GET.get('page')
    try:
        blog_list=paginator.page(page)
    except PageNotAnInteger:
        blog_list=paginator.page(1)
    except EmptyPage:  # 如果页码太大，没有相应的记录
         blog_list=paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'blog_list':blog_list,'tags':tags})

def bolg(request,id=''):
    prev=False
    next=False
    tags=Tag.objects.all()
    try:
        blog=Blog.objects.get(id=id)
        if int(id)!=1:
            next=Blog.objects.get(id=int(id)-1)
        blogs=Blog.objects.all()
        if int(id)+1<=blogs[0].id:
            prev=Blog.objects.get(id=int(id)+1)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response('blog_show.html',{'blog':blog,'prev':prev,'next':next,'tags':tags})

def about(request):
     tags=Tag.objects.all()
     return render_to_response('about.html',{'tags':tags})
