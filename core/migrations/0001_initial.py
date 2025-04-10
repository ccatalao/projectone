# Generated by Django 5.0.7 on 2024-07-23 15:15

import core.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, null=True)),
                ('html_content', models.TextField(blank=True, null=True)),
                ('img_link', models.CharField(blank=True, max_length=200, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=core.models.upload_directory)),
                ('image_file', models.FileField(blank=True, null=True, upload_to=core.models.upload_directory)),
                ('category', models.TextField(blank=True, help_text='Separate each item by comma', null=True)),
                ('img_label', models.TextField(blank=True, help_text='Separate each item by comma', null=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('is_digital', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
