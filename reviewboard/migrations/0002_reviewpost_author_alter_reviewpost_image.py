# Generated by Django 4.2 on 2023-05-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpost',
            name='author',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reviewpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
