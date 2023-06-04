# Generated by Django 4.2 on 2023-05-28 11:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewboard', '0004_reviewpost_liked_users_reviewpost_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpost',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='reviewpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='like_user',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
