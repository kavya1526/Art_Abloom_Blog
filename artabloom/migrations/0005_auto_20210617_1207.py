# Generated by Django 3.1.7 on 2021-06-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artabloom', '0004_auto_20210616_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='static/img/'),
        ),
    ]