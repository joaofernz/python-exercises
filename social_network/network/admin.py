from django.contrib import admin

from .models import Comment, Post, Profile

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
