# Generated by Django 4.0.1 on 2022-06-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_dateideas_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateideas',
            name='image',
            field=models.TextField(default='', null=True),
        ),
    ]
