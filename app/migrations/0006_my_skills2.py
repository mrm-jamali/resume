# Generated by Django 5.0 on 2023-12-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_why_trust'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_skills2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(null=True, upload_to='media/app')),
            ],
        ),
    ]
