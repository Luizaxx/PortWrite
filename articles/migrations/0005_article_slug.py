# Generated by Django 5.1 on 2024-09-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_articlevideo_article_article_image_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
