from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='comments',
        to=User
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )
    post = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='comments',
        to='Post'
    )
    text = models.TextField()


class Follow(models.Model):
    user = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='followers',
        to=User
    )
    following = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='follow',
        to=User
    )


class Group(models.Model):
    description = models.TextField()
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='posts',
        to=User
    )
    group = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
        to=Group
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='posts/'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField()

    def __str__(self):
        return self.text
