from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    basename='posts',
    prefix=r'^posts',
    viewset=PostViewSet
)
router_v1.register(
    basename='groups',
    prefix=r'^groups',
    viewset=GroupViewSet
)
router_v1.register(
    basename='follow',
    prefix=r'^follow',
    viewset=FollowViewSet
)
router_v1.register(
    basename='comment',
    prefix=r'^posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet
)


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
