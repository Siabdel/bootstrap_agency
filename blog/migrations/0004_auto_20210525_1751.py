# Generated by Django 3.1.10 on 2021-05-25 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_bloglistingpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='date',
            new_name='created',
        ),
    ]