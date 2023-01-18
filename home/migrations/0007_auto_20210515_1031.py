# Generated by Django 3.1.10 on 2021-05-15 10:31

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_banner_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]