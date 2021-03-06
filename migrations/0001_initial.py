# Generated by Django 2.2 on 2018-08-19 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medium', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='timestamp')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('media', models.ManyToManyField(related_name='media_post', to='medium.Medium')),
            ],
            options={
                'db_table': 'post',
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.CreateModel(
            name='WallPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_wallpost', to='post.Post')),
                ('waller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waller_wallpost', to=settings.AUTH_USER_MODEL, verbose_name='Waller')),
            ],
            options={
                'db_table': 'wall_post',
            },
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='timestamp')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor_commentpost', to=settings.AUTH_USER_MODEL, verbose_name='Commentor')),
                ('commentpost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentpost_commentpost', to='post.CommentPost')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_commentpost', to='post.Post')),
            ],
            options={
                'db_table': 'comment_post',
            },
        ),
    ]
