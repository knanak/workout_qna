# Generated by Django 4.1.9 on 2023-05-12 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("curation", "0008_result_vaule_alter_answer_vaule_alter_result_youtube"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="vaule",
            new_name="value",
        ),
    ]