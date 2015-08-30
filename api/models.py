from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to="%Y/%m/%d")

    def __unicode__(self):
        return self.post.title

    def post_author(self):
        return self.post.author

    def show_photo(self):
        return """<img src='%s' width=100 height=100>""" % self.image.url

    show_photo.allow_tags = True
