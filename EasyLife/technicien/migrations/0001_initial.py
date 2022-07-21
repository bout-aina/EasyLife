# Generated by Django 3.2 on 2021-05-06 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technicien',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mdp', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=30)),
                ('cin', models.CharField(max_length=30)),
                ('domaine', models.CharField(max_length=30)),
                ('diplome', models.CharField(max_length=30)),
                ('idAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.admin')),
            ],
        ),
    ]