# Generated by Django 3.1.7 on 2021-06-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artabloom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
    ]
