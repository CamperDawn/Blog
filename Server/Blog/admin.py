from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Comment, Post, Profile

# Register your models here.

#class ProfileUser(admin.ModelAdmin):


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
