# Generated by Django 3.2 on 2021-06-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sentBy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]