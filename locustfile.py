# import os
# import sys

from locust import HttpUser, task, between

# sys.path.append('/Users/p.ushakov/projects/personal/django-blog-perf')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog_perf.settings'
# from django.db.models import Max, Min
# from blog_app.models import BlogPost
# import django
# django.setup()


class QuickstartUser(HttpUser):
    # wait_time = between(1, 2.5)

    @task
    def main_page(self):
        self.client.get('/')


    @task(3)
    def post_page(self):
        for post_id in range(1012, 1511):
            self.client.get(f'/post/{post_id}')


# def get_blog_posts_ids_range():
#     return BlogPost.objects.aggregate(max_id=Max('id'), min_id=Min('id'))
