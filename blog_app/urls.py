from django.urls import path

from blog_app import views


urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('post/<int:post_id>', views.post_details, name='post_details'),
]