# Generated by Django 4.2.13 on 2024-05-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_video_script'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='extra_img_name1',
        ),
        migrations.RemoveField(
            model_name='video',
            name='extra_img_name2',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_img_name',
        ),
        migrations.AddField(
            model_name='video',
            name='file_name',
            field=models.TextField(default=''),
        ),
    ]
