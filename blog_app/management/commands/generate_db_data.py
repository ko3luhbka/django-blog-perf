from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from blog_app.models import User, BlogPost, BlogPostComment


NUM_OF_USERS = 50
POSTS_PER_USER = 10
TEST_STRING = 'lorem ipsum'


class Command(BaseCommand):

    def handle(self, *args, **options):
        with transaction.atomic():
            create_em_all()
        print('Done!')


def create_user(username: str):
    password = '123'
    return User.objects.create(username=username, password=password)


def create_blog_post(author: User):
    post_content = 15 * TEST_STRING
    post_title = 2 * TEST_STRING
    return BlogPost.objects.create(
        title=post_title,
        content=post_content,
        author=author,
        status=BlogPost.STATUS_PUBLISHED,
    )


def create_post_comment(post: BlogPost, author: User):
    comment_content = 10 * TEST_STRING
    return BlogPostComment.objects.create(
        content=comment_content,
        author=author,
        blog_post=post,
    )


def create_em_all():
    for user_num in range(NUM_OF_USERS):
        user = create_user(f'User_{user_num}')
        for post_num in range(POSTS_PER_USER):
            post = create_blog_post(author=user)
        print(f'{post_num + 1} posts are created for user {user}')
    print(f'{user_num + 1} users are created')


    for user in User.objects.all():
        for post in BlogPost.objects.all():
            create_post_comment(post=post, author=user)
    print('Comments are created')
    
