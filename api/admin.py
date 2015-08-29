from django.contrib import admin
from .models import MyUser, Post, Photo

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Photo)
