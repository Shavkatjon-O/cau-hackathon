# Generated by Django 5.0.7 on 2024-11-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="activity_level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Sedentary", "Sedentary"),
                    ("Light", "Light"),
                    ("Moderate", "Moderate"),
                    ("Active", "Active"),
                    ("Very Active", "Very Active"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="allergies",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="dietary_preferences",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="goal",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Weight Loss", "Weight Loss"),
                    ("Muscle Gain", "Muscle Gain"),
                    ("Maintain", "Maintain"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="height",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="weight",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]