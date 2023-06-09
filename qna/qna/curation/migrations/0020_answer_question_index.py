# Generated by Django 4.1.9 on 2023-05-25 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("curation", "0019_remove_question_question_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="question_index",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="index_a",
                to="curation.questionindex",
            ),
        ),
    ]
