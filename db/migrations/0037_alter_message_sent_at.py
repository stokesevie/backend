# Generated by Django 4.1.5 on 2023-02-24 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0036_alter_lab_lab_id_alter_message_related_lab_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 24, 10, 12, 4, 662947)
            ),
        ),
    ]