from django.contrib import admin
from Blog.models import *
# Register your models here.

admin.site.register(Author,AuthorAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag,TagAdmin)
