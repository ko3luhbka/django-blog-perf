from django.shortcuts import render, get_object_or_404


from blog_app.models import BlogPost, BlogPostComment, User


def all_posts(request):
    posts = BlogPost.objects.filter(status=BlogPost.STATUS_PUBLISHED)
    return render(request, 'blog_app/all_posts_page.html', context={'posts': posts})


def post_details(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_app/post_page.html', context={'post': post})
