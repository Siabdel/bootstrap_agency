# Generated by Django 3.1.10 on 2021-05-17 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_menu_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
