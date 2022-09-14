from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content', 'time_create', 'cover')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('id','titles')

admin.site.register(News, NewsAdmin)
admin.site.register(Themes, ThemesAdmin)