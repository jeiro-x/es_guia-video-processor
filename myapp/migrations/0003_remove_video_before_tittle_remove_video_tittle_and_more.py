# Generated by Django 5.0.4 on 2024-05-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_guias_guia_rename_vieos_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='before_tittle',
        ),
        migrations.RemoveField(
            model_name='video',
            name='tittle',
        ),
        migrations.RemoveField(
            model_name='video',
            name='total_items',
        ),
        migrations.AddField(
            model_name='video',
            name='code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='extension',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='video',
            name='num_items',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=70),
        ),
    ]