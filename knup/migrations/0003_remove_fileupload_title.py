# Generated by Django 3.1.3 on 2020-11-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knup', '0002_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='title',
        ),
    ]
