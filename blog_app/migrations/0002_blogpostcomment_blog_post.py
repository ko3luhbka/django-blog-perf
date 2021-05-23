# Generated by Django 3.2.3 on 2021-05-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostcomment',
            name='blog_post',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='blog_app.blogpost',
            ),
            preserve_default=False,
        ),
    ]