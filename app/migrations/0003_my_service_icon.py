# Generated by Django 5.0 on 2023-12-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_my_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_service',
            name='icon',
            field=models.ImageField(null=True, upload_to='media/app'),
        ),
    ]
