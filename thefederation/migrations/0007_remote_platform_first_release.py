# Generated by Django 2.0.3 on 2018-04-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thefederation', '0006_add_platform_install_guide_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='first_release',
        ),
    ]
