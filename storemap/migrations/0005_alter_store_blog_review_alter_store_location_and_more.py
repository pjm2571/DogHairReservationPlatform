# Generated by Django 4.2.1 on 2023-05-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemap', '0004_store_latitude_store_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='blog_review',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='store',
            name='open_hours',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='store',
            name='visitor_review',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='store',
            name='website',
            field=models.TextField(default=''),
        ),
    ]
