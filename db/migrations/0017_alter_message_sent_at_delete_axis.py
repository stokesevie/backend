# Generated by Django 4.1.5 on 2023-02-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0016_alter_message_sent_at_axis_average"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(default="2023-02-17 13:29:28Z"),
        ),
        migrations.DeleteModel(
            name="axis",
        ),
    ]
