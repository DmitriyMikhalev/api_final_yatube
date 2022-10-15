import base64

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        super().to_internal_value(data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('id', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    user = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        user = self.context['request'].user
        to_follow = get_object_or_404(
            klass=User,
            username=data['following'].username
        )

        if user == to_follow:
            raise ValidationError('You can\'t follow yourself.')

        if Follow.objects.filter(user=user, following=to_follow).exists():
            raise ValidationError('You have already followed.')

        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group
        read_only_fields = fields


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post
        read_only_fields = ('id', 'author', 'pub_date')
