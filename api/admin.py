from django.contrib import admin
from .models import Profile, Post, Photo

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('post', 'post_author', 'show_photo')

admin.site.register(Profile)
admin.site.register(Photo, PhotoAdmin)
