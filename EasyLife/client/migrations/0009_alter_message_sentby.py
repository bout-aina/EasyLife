# Generated by Django 3.2 on 2021-06-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_message_sentby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sentBy',
            field=models.CharField(max_length=1),
        ),
    ]
