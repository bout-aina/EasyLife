# Generated by Django 3.2 on 2021-05-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('sujet', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=30)),
            ],
        ),
    ]