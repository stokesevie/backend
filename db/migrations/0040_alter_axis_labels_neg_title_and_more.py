# Generated by Django 4.1.5 on 2023-02-27 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0039_alter_message_related_lab_alter_message_sent_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="axis_labels",
            name="neg_title",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="axis_labels",
            name="pos_title",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 27, 15, 37, 16, 889692)
            ),
        ),
    ]
