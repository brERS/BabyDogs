# Generated by Django 4.1.7 on 2023-03-13 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0002_remove_subnavcontent_additional_js_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subnav',
            name='additional_js',
        ),
        migrations.RemoveField(
            model_name='subnav',
            name='is_home',
        ),
    ]
