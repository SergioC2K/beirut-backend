# Generated by Django 5.0.7 on 2024-08-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beirutAdmin', '0006_alter_gallery_url_alter_specialevents_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeirutVideos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('video_url', models.FileField(max_length=500, upload_to='videos')),
            ],
        ),
    ]
