# Generated by Django 3.2.3 on 2021-06-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_food_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]