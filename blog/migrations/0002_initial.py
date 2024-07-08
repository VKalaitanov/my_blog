# Generated by Django 5.0.6 on 2024-07-08 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.tagpost', verbose_name='Теги'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-time_create'], name='blog_post_time_cr_cc1db6_idx'),
        ),
    ]
