# Generated by Django 4.1.5 on 2023-02-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0023_rename_student_id_tutor_teaching_tutor_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(default="2023-02-20 18:49:10Z"),
        ),
    ]
