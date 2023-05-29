# Generated by Django 4.1.9 on 2023-05-28 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("curation", "0023_question_question_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="autor_q",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
