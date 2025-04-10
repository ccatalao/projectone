# Generated by Django 5.0.7 on 2025-04-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_content_post_description_post_lide_post_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
