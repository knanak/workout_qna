# Generated by Django 4.1.9 on 2023-05-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_usertype_alter_user_name_user_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_name",
            field=models.CharField(max_length=255, null=True, verbose_name="Name of User"),
        ),
    ]