# Generated by Django 4.2.4 on 2023-08-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.FloatField()),
                ('potassium', models.FloatField()),
                ('calcium', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('soil_ph', models.FloatField()),
                ('ground_precipitation', models.FloatField()),
                ('available_water_annual', models.FloatField()),
                ('classification', models.FloatField()),
            ],
        ),
    ]
