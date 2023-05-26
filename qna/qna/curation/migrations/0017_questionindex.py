# Generated by Django 4.1.9 on 2023-05-25 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("curation", "0016_question_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionIndex",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("create", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=400, null=True)),
                (
                    "question",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="index_q",
                        to="curation.question",
                    ),
                ),
                (
                    "question_category",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="curation.questioncategory"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
