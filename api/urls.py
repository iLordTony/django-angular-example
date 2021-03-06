from django.conf.urls import url, include

from api.views import UserList, PostDetail, PostList, UserPostList, UserDetail, PostPhotoList, PhotoList, PhotoDetail

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

users_urls = [
    url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/posts/$', UserPostList.as_view(), name='userpost-list'),
]

posts_urls = [
    url(r'^$', PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/photos/$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
]

photos_urls = [
    url(r'^(?P<pk>\d+)/$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list'),
]

urlpatterns = [
    url(r'^users/', include(users_urls)),
    url(r'^posts/', include(posts_urls)),
    url(r'^photos/', include(photos_urls)),
]
