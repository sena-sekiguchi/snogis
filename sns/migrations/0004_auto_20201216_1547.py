# Generated by Django 3.1.4 on 2020-12-16 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_auto_20201216_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='menber',
            new_name='menberlist',
        ),
    ]