# Generated by Django 4.0.1 on 2022-06-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('priority', models.IntegerField()),
                ('duration', models.CharField(choices=[('short', 'short'), ('medium', 'medium'), ('long', 'long')], default='short', max_length=6)),
                ('check_done', models.BooleanField(default=False)),
                ('review', models.TextField(default='')),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('date_done', models.DateField(default=None, null=True)),
            ],
        ),
    ]
