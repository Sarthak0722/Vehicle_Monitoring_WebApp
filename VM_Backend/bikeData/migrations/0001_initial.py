# Generated by Django 5.0.7 on 2024-07-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('number_plate', models.CharField(max_length=50)),
                ('assigned_driver', models.CharField(max_length=100)),
            ],
        ),
    ]
