from django.conf.urls import url, include
from rest_framework import routers
from api.views import PostsViewSet, PhotosViewSet

router = routers.DefaultRouter()
router.register(r'photos', PhotosViewSet, base_name='photo-list')
router.register(r'posts', PostsViewSet)


#router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]