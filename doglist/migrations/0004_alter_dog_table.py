# Generated by Django 4.2.1 on 2023-05-29 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doglist', '0003_alter_dog_img_src'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dog',
            table='doglist_dog',
        ),
    ]
