# Generated by Django 3.2.9 on 2021-11-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_neighbourhood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood_events',
            name='person',
        ),
    ]
