from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (GenericViewSet,
                                     ModelViewSet,
                                     ReadOnlyModelViewSet)

from .serializers import (CommentSerializer,
                          FollowSerializer,
                          GroupSerializer,
                          PostSerializer)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(id=post_id, klass=Post)

        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(id=post_id, klass=Post)

        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ('=user__username', '=following__username')
    serializer_class = FollowSerializer

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PostViewSet(ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
