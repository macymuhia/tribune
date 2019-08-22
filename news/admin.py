from django.contrib import admin
from .models import Editor, Article, tag

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)


admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tag)
