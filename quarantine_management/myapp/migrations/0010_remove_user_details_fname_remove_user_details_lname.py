# Generated by Django 4.2.1 on 2023-05-26 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_owner_details_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='lname',
        ),
    ]