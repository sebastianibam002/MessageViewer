# Generated by Django 4.0.1 on 2022-06-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateideas',
            name='image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]