# Generated by Django 3.2.3 on 2021-06-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]