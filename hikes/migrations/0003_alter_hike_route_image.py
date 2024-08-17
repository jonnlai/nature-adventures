# Generated by Django 4.2.15 on 2024-08-17 16:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0002_hike_route_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='route_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
