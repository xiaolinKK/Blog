from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
# Create your models here.

class Tag(models.Model):
    tag_name=models.CharField('标签',max_length=20,blank=True)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)

class TagAdmin(admin.ModelAdmin):
    list_display=('tag_name','create_time')

class Author(models.Model):
    name=models.CharField('名字',max_length=30)
    email=models.EmailField('邮箱',blank=True)
    website=models.URLField('博客',blank=True)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','email','website')
    search_fields=('name','email')


class Blog(models.Model):
    caption=models.CharField('标题',max_length=50)
    author=models.ForeignKey(Author)
    tags=models.ManyToManyField(Tag,blank=True)
    content=models.TextField('内容')
    publish_time=models.DateTimeField('发表时间',auto_now_add=True)
    update_time=models.DateTimeField('更新时间',auto_now=True)

    def get_authorname(self,obj):
        return obj.author.name
    get_authorname.short_description='作者'

    def get_absolute_url(self):
        path = reverse('detailblog', kwargs={'id':self.id})
        return "http://127.0.0.1:8080%s" % path

    class Meta:
        ordering = ['-publish_time']



class BlogAdmin(admin.ModelAdmin):
    list_display = ('caption','get_authorname','publish_time')
    list_filter = ('publish_time',)
    #date_hierarchy =( 'publish_time')
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

    def get_authorname(self,obj):
        return obj.author.name
    get_authorname.short_description='作者'

    