from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    viewset=PostViewSet,
    prefix=r'^posts'
)
router_v1.register(
    viewset=GroupViewSet,
    prefix=r'^groups'
)
router_v1.register(
    viewset=FollowViewSet,
    prefix=r'^follow',
    basename='follow'
)
router_v1.register(
    viewset=CommentViewSet,
    prefix=r'^posts/(?P<post_id>\d+)/comments',
    basename='comment'
)


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]
