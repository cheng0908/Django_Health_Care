# Generated by Django 3.2.3 on 2021-06-09 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitforum', '0002_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='level',
        ),
    ]
