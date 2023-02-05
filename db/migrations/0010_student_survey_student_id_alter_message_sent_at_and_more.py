# Generated by Django 4.1.5 on 2023-02-05 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0009_alter_message_sent_at_alter_student_lab_risk_axis_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_survey",
            name="student_id",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="db.student"
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(default="2023-02-05 15:30:50Z"),
        ),
        migrations.CreateModel(
            name="question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "x",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="x",
                        to="db.axis_labels",
                    ),
                ),
                (
                    "y",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="y",
                        to="db.axis_labels",
                    ),
                ),
            ],
        ),
    ]
