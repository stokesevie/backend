# Generated by Django 4.1.5 on 2023-02-23 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0032_alter_message_sent_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 23, 19, 15, 55, 477301)
            ),
        ),
    ]
