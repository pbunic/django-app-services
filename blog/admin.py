from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['-status', '-publish']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '72'})},
    }
