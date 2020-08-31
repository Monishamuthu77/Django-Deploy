# Generated by Django 3.0.8 on 2020-07-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('phone', models.BigIntegerField(unique=True)),
                ('aadhar', models.BigIntegerField(unique=True)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
