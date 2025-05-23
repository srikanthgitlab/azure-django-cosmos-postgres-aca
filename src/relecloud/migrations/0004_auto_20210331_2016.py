# Generated by Django 3.1.7 on 2021-03-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("relecloud", "0003_auto_20210331_1932"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inforequest",
            name="name",
            field=models.CharField(max_length=50),
        ),migrations.AlterField(
            model_name='restaurant',
            name='image_name',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='image_name',
            field=models.UUIDField(),
        ),
    ]
