# Generated by Django 3.1.10 on 2022-02-21 17:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('menu', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0031_auto_20220221_1759'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceStremFieldPage',
            new_name='ServiceStreamFieldPage',
        ),
    ]
