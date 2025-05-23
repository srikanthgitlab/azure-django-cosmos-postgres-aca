# Generated by Django 4.2.4 on 2023-08-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("relecloud", "0005_cruise_subtitle_destination_subtitle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cruise",
            name="subtitle",
            field=models.CharField(blank=True, max_length=240),
        ),
        migrations.AlterField(
            model_name="destination",
            name="subtitle",
            field=models.CharField(blank=True, max_length=240),
        ),migrations.AlterField(
            model_name='review',
            name='image_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
