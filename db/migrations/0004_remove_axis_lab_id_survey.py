# Generated by Django 4.1.5 on 2023-01-16 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0003_lab_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="axis",
            name="lab_id",
        ),
        migrations.CreateModel(
            name="survey",
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
                    "question_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_1",
                        to="db.axis_labels",
                    ),
                ),
                (
                    "question_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_2",
                        to="db.axis_labels",
                    ),
                ),
                (
                    "question_3",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_3",
                        to="db.axis_labels",
                    ),
                ),
            ],
        ),
    ]
