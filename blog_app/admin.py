from django.contrib import admin

from blog_app.models import BlogPost, BlogPostComment, User


admin.site.register(BlogPost)
admin.site.register(BlogPostComment)
admin.site.register(User)
