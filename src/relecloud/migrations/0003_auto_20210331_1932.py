# Generated by Django 3.1.7 on 2021-03-31 19:32

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):
    dependencies = [
        ("relecloud", "0002_auto_20210330_2200"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cruise",
            name="destinations",
            field=models.ManyToManyField(related_name="cruises", to="relecloud.Destination"),
        ),migrations.AddField(
            model_name='restaurant',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('24ba6836-5acb-4e64-961a-b994de8cfb01')),
        ),
        migrations.AddField(
            model_name='review',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('58977b57-8293-4a84-bccc-34ef7bb138a4')),
        ),
    ]
