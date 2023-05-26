# Generated by Django 4.2.1 on 2023-05-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_date_needed_booking_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner_details',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='document',
            field=models.FileField(null=True, upload_to='ownerdocs'),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='fname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='status',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='owner_details',
            name='user_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]