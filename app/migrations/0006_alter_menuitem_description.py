# Generated by Django 5.1.2 on 2025-01-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_menuitem_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]