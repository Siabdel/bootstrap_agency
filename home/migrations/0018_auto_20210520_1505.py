# Generated by Django 3.1.10 on 2021-05-20 13:05

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210520_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extratext',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Unique identifier', populate_from='name'),
        ),
    ]
