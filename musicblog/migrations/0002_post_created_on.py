# Generated by Django 3.2 on 2022-04-18 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("musicblog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_on",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
