from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class BlogPost(models.Model):
    STATUS_PUBLISHED, STATUS_DRAFT = [str(num) for num in range(2)]

    STATUS_CHOICES = [
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_DRAFT, 'Draft'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4096)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_DRAFT)


class BlogPostComment(models.Model):
    content = models.TextField(max_length=4096)
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    blog_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
    )
