# Generated by Django 4.1.5 on 2023-01-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lab",
            name="lab_id",
            field=models.IntegerField(
                default="1", max_length=10, primary_key=True, serialize=False
            ),
        ),
    ]
